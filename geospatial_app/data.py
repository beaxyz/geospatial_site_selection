
import os
from databricks import sql
from databricks.sdk.core import Config
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
#from pyspark.sql import functions as F

assert os.getenv("DATABRICKS_WAREHOUSE_ID"), "DATABRICKS_WAREHOUSE_ID is not set"

#load_dotenv()
cfg = Config()

def is_local_environment() -> bool:
    return not os.getenv("DATABRICKS_WAREHOUSE_ID")


def sql_query(query: str, user_token: str) -> pd.DataFrame:
    if is_local_environment():
        connection_args = {
        "server_hostname": os.getenv("DATABRICKS_HOST"),
        "http_path": f"/sql/1.0/warehouses/{os.getenv('DATABRICKS_WAREHOUSE_ID')}",
        "access_token": os.getenv("DATABRICKS_TOKEN")
    }

    else:
        connection_args = {
        "server_hostname": cfg.host,
        "http_path": f"/sql/1.0/warehouses/{cfg.warehouse_id}",
        "access_token": user_token
    }

    with sql.connect(**connection_args) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall_arrow().to_pandas()

user_token = st.context.headers.get('X-Forwarded-Access-Token')

@st.cache_data()
def developed_land_df(general_land_type: str = "All") -> pd.DataFrame:
    query = """
    select * from beatrice_liew.site_selection_geospatial.developed_land_silver
    """
    
    if general_land_type != "All":
        query += f" where general_land_type = '{general_land_type}'"
    else:
        query = query

    return sql_query(query, user_token = user_token)

square_size_m2 = 1000

@st.cache_data()
def undeveloped_land_df(general_land_type: str = "All") -> pd.DataFrame:
    query = """
    select *
    from beatrice_liew.site_selection_geospatial.undeveloped_land_silver
    """ 
    
    if general_land_type != "All":
        query += f" where general_land_type = '{general_land_type}'"
    else:
        query = query

    return sql_query(query,user_token)

@st.cache_data()
def road_node_df() -> pd.DataFrame:
    query = """
    select *
    from beatrice_liew.site_selection_geospatial.road_node_silver
    """
    return sql_query(query, user_token)

@st.cache_data()
def road_links_df() -> pd.DataFrame:
    query = """
    select *
    from beatrice_liew.site_selection_geospatial.road_links_silver
    """
    return sql_query(query, user_token)

@st.cache_data()
def bounding_box_df(general_land_type: str = "All", square_size_m2: int = 3000, number_of_sites: int = 10, distance_to_road_min: int = 100, distance_to_road_max: int = 1000) -> pd.DataFrame:
    
    if general_land_type != "All":
        query = f"""with bounding_options as (
                    select * from beatrice_liew.site_selection_geospatial.undeveloped_land_silver_distance_to_road
                    where geometry_area_m2 >= {square_size_m2} and 
                    distance_to_road_meters >= {distance_to_road_min} and
                    distance_to_road_meters <= {distance_to_road_max}
                    order by distance_to_road_meters asc
                    ),
                    
                    bounding_options_distance as (
                    select osid, toid, general_land_type, min(distance_to_road_meters) as distance_to_road_meters
                    from bounding_options
                    group by osid, toid, general_land_type
                    order by distance_to_road_meters asc
                    ),

                    join_bounding_options_distance_to_road as (
                    select a.osid, a.toid, a.general_land_type, b.geometry_area_m2, a.distance_to_road_meters, b.geometry, b.centroid_bng
                    from bounding_options_distance a
                    left join bounding_options b 
                    on a.osid = b.osid and a.toid = b.toid and a.distance_to_road_meters = b.distance_to_road_meters
                    )

                    select osid, toid, general_land_type, geometry_area_m2, st_astext(geometry) as geometry, st_astext(st_transform(st_envelope(st_buffer(centroid_bng, (sqrt({square_size_m2})/2))), 4326)) as geometry_box, distance_to_road_meters
                    from join_bounding_options_distance_to_road
                    where general_land_type = '{general_land_type}
                    order by distance_to_road_meters asc
                    limit {number_of_sites}

                    """
    else:
        query = f"""with bounding_options as (
                    select * from beatrice_liew.site_selection_geospatial.undeveloped_land_silver_distance_to_road
                    where geometry_area_m2 >= {square_size_m2} and 
                    distance_to_road_meters >= {distance_to_road_min} and
                    distance_to_road_meters <= {distance_to_road_max}
                    order by distance_to_road_meters asc
                    ),
                    
                    bounding_options_distance as (
                    select osid, toid, min(distance_to_road_meters) as distance_to_road_meters
                    from bounding_options
                    group by osid, toid
                    order by distance_to_road_meters asc
                    ),

                    join_bounding_options_distance_to_road as (
                    select a.osid, a.toid, b.geometry_area_m2, a.distance_to_road_meters, b.geometry, b.centroid_bng
                    from bounding_options_distance a
                    left join bounding_options b 
                    on a.osid = b.osid and a.toid = b.toid and a.distance_to_road_meters = b.distance_to_road_meters
                    )

                    select 
                    osid, 
                    toid, 
                    geometry_area_m2, 
                    st_astext(geometry) as geometry, 
                    st_astext(st_transform(st_envelope(st_buffer(centroid_bng, (sqrt({square_size_m2})/2))), 4326)) as geometry_box, 
                    distance_to_road_meters
                    from join_bounding_options_distance_to_road
                    order by distance_to_road_meters asc
                    limit {number_of_sites}"""

    return sql_query(query, user_token)

if __name__ == "__main__":
    print(bounding_box_df(square_size_m2=1000, distance_to_road=1000, number_of_sites=10, general_land_type="All"))
