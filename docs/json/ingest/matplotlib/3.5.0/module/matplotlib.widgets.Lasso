{
  "_content": {
    "Attributes": {
      "children": [],
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
                  "value": "The selected path can be used in conjunction with "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "~matplotlib.path.Path.contains_point",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.0",
                    "kind": "module",
                    "path": "matplotlib.path.Path.contains_point"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " to select data points from an image."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Unlike "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "LassoSelector",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.0",
                    "kind": "module",
                    "path": "matplotlib.widgets.LassoSelector"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", this must be initialized with a starting point "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "xy"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", and the "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "Lasso",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.0",
                    "kind": "module",
                    "path": "matplotlib.widgets.Lasso"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " events are destroyed upon release."
                }
              }
            ],
            "inner": []
          }
        }
      ],
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
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "ax",
            "type_": "`~matplotlib.axes.Axes`",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The parent axes for the widget."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "xy",
            "type_": "(float, float)",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Coordinates of the start of the lasso."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "useblit",
            "type_": "bool, default: True",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether to use blitting for faster drawing (if supported by the backend)."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "callback",
            "type_": "callable",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whenever the lasso is released, the "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "callback"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " function is called and passed the vertices of the selected path."
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
    "Raises": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [],
      "title": null
    },
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Selection curve of an arbitrary shape."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Warnings": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    }
  },
  "refs": [
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.widgets.LassoSelector"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.path.Path.contains_point"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.widgets.Lasso"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters"
  ],
  "item_file": "/matplotlib/widgets.py",
  "item_line": 3619,
  "item_type": "<class 'type'>",
  "aliases": [
    "matplotlib.widgets.Lasso"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "3.5.0",
  "signature": "Lasso(ax, xy, callback=None, useblit=True)",
  "references": null,
  "logo": "logo.png",
  "qa": "matplotlib.widgets.Lasso",
  "arbitrary": []
}