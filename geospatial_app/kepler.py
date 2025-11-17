from typing import Dict
import pandas as pd
from keplergl import KeplerGl

config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "Bounding Box",
          "type": "geojson",
          "config": {
            "dataId": "Bounding Box",
            "columnMode": "geojson",
            "label": "Bounding Box",
            "color": [0, 200, 0],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "geojson": "geometry_box"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1.0,
              "strokeOpacity": 1.0,
              "thickness": 1.0,
              "strokeColor": [0, 200, 0],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False,
              "fixedHeight": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center",
                "outlineWidth": 0,
                "outlineColor": [
                  255,
                  0,
                  0,
                  255
                ],
                "background": False,
                "backgroundColor": [
                  0,
                  0,
                  200,
                  255
                ]
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "Bounding Box Area",
          "type": "geojson",
          "config": {
            "dataId": "Bounding Box",
            "columnMode": "geojson",
            "label": "Bounding Box Area",
            "color": [144, 238, 144],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1.0,
              "strokeOpacity": 1.0,
              "thickness": 1.0,
              "strokeColor": [144, 238, 144],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False,
              "fixedHeight": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center",
                "outlineWidth": 0,
                "outlineColor": [
                  255,
                  0,
                  0,
                  255
                ],
                "background": False,
                "backgroundColor": [
                  0,
                  0,
                  200,
                  255
                ]
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "Developed",
          "type": "geojson",
          "config": {
            "dataId": "Developed",
            "columnMode": "geojson",
            "label": "Developed",
            "color": [173, 216, 230],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "geojson": "geometry_wgs84"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [0, 0, 139],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False,
              "fixedHeight": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center",
                "outlineWidth": 0,
                "outlineColor": [
                  255,
                  0,
                  0,
                  255
                ],
                "background": False,
                "backgroundColor": [
                  0,
                  0,
                  200,
                  255
                ]
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "Undeveloped Land",
          "type": "geojson",
          "config": {
            "dataId": "Undeveloped Land",
            "columnMode": "geojson",
            "label": "Undeveloped Land",
            "color": [210, 180, 140],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "geojson": "geometry_wgs84"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.5,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [139, 119, 101],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#4C0035",
                  "#880030",
                  "#B72F15",
                  "#D6610A",
                  "#EF9100",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False,
              "fixedHeight": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center",
                "outlineWidth": 0,
                "outlineColor": [
                  255,
                  0,
                  0,
                  255
                ],
                "background": False,
                "backgroundColor": [
                  0,
                  0,
                  200,
                  255
                ]
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "road-nodes",
          "type": "geojson",
          "config": {
            "dataId": "Road Nodes",
            "columnMode": "geojson",
            "color": [255, 165, 0],
            "columns": {
              "geojson": "geometry_wgs_84"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1.0,
              "strokeOpacity": 1.0,
              "thickness": 0.3,
              "strokeColor": [255, 165, 0]
            }
          }
        },
        {
          "id": "road-links",
          "type": "geojson",
          "config": {
            "dataId": "Road Links",
            "columnMode": "geojson",
            "color": [255, 165, 0],
            "columns": {
              "geojson": "geometry_wgs84"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1.0,
              "strokeOpacity": 1.0,
              "thickness": 0.5,
              "strokeColor": [255, 165, 0]
            }
          }
        }
      ],
      "effects": [],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Developed": [
              {
                "name": "general_land_type",
                "format": None
              },
              {
                "name": "detailed_land_type",
                "format": None
              },
              {
                "name": "geometry_area_m2",
                "format": None
              }
            ],
            "Undeveloped Land": [
              {
                "name": "general_land_type",
                "format": None
              },
              {
                "name": "detailed_land_type",
                "format": None
              }
            ],
            "Bounding Box": [
              {
                "name": "osid",
                "format": None
              },
              {
                "name": "toid",
                "format": None
              },
              {
                "name": "geometry_area_m2",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "overlayBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      },
      "editor": {
        "features": [],
        "visible": True
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 50.72167793577414,
      "longitude": -3.5350724553588573,
      "pitch": 0,
      "zoom": 14.258374861528521,
      "isSplit": False,
      "isViewportSynced": True,
      "isZoomLocked": False,
      "splitMapViewports": []
    },
    "mapStyle": {
      "styleType": "dark-matter",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        15.035172933000911,
        15.035172933000911,
        15.035172933000911
      ],
      "backgroundColor": [
        0,
        0,
        0
      ],
      "mapStyles": {}
    },
    "uiState": {
      "mapControls": {
        "mapLegend": {
          "active": False
        }
      }
    }
  }
}


def render_kepler(data: Dict[str, pd.DataFrame], config=config, height=800, width=500) -> KeplerGl:
    kmap = KeplerGl(height=height, width=width)

    for name, df in data.items():
        kmap.add_data(name=name, data=df)

    kmap.config = config
    return kmap


def kepler_html(kmap: KeplerGl) -> str:
    html = kmap._repr_html_()
    if isinstance(html, bytes):
        html = html.decode("utf-8")

    html = (
        html
        .replace("\.height\|\|\d+", f".height||{kmap.height}")
        .replace("#container {width: 300px;", "#container {width: 100%;")
    )

    html += "<script>window.dispatchEvent(new Event('resize'));</script>"
    return html


