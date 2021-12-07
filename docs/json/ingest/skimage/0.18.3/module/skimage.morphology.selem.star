{
  "_content": {
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Generates a star shaped structuring element."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Extended Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Start has 8 vertices and is an overlap of square of size "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": [
                    "2*a + 1"
                  ],
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " with its 45 degree rotated version. The slanted sides are 45 or 135 degrees to the horizontal axis."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "a",
            "type_": "int",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Parameter deciding the size of the star structural element. The side of the square array returned is "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "2",
                          "*",
                          "a",
                          " ",
                          "+",
                          " ",
                          "1",
                          " ",
                          "+",
                          " ",
                          "2",
                          "*",
                          "floor(a",
                          " ",
                          "/",
                          " ",
                          "2)"
                        ],
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Returns": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "selem",
            "type_": "ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The structuring element where elements of the neighborhood are 1 and 0 otherwise."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Raises": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Other Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "dtype",
            "type_": "data-type",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The data type of the structuring element."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Attributes": {
      "children": [],
      "title": null
    },
    "Methods": {
      "children": [],
      "title": null
    },
    "Notes": {
      "children": [],
      "title": null
    },
    "Warnings": {
      "children": [],
      "title": null
    }
  },
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Other Parameters",
    "Returns"
  ],
  "item_file": "/Users/bussonniermatthias/miniconda3-intel/envs/papyri/lib/python3.9/site-packages/skimage/morphology/selem.py",
  "item_line": 303,
  "item_type": "<class 'function'>",
  "aliases": [
    "skimage.morphology.star"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "0.18.3",
  "signature": "star(a, dtype=<class 'numpy.uint8'>)",
  "references": null,
  "logo": "logo.png",
  "qa": "skimage.morphology.selem.star",
  "arbitrary": []
}