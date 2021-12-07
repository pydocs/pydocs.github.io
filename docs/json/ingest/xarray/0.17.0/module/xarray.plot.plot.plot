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
                  "value": "Default plot of DataArray using matplotlib.pyplot."
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
                  "value": "Calls xarray plotting function based on the dimensions of darray.squeeze()"
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
                  "value": "=============== =========================== Dimensions      Plotting function --------------- --------------------------- 1               "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "xarray.plot.line",
                  "reference": {
                    "module": "xarray",
                    "version": "0.17.0",
                    "kind": "module",
                    "path": "xarray.plot.plot.line"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " 2               "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "xarray.plot.pcolormesh",
                  "reference": {
                    "module": "xarray",
                    "version": "0.17.0",
                    "kind": "module",
                    "path": "xarray.plot.plot.pcolormesh"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " Anything else   "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "xarray.plot.hist",
                  "reference": {
                    "module": "xarray",
                    "version": "0.17.0",
                    "kind": "module",
                    "path": "xarray.plot.plot.hist"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " =============== ==========================="
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
            "param": "darray",
            "type_": "DataArray",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "row",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If passed, make row faceted plots on this dimension name"
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
            "param": "col",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If passed, make column faceted plots on this dimension name"
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
            "param": "hue",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If passed, make faceted line plots with hue on this dimension name"
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
            "param": "col_wrap",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Use together with "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "col"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " to wrap faceted plots"
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
            "param": "ax",
            "type_": "matplotlib.axes.Axes, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If None, uses the current axis. Not applicable when using facets."
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
            "param": "rtol",
            "type_": "float, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Relative tolerance used to determine if the indexes are uniformly spaced. Usually a small positive number."
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
            "param": "subplot_kws",
            "type_": "dict, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Dictionary of keyword arguments for matplotlib subplots."
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
            "param": "**kwargs",
            "type_": "optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Additional keyword arguments to matplotlib"
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
      "children": [],
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
      "children": [],
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
  "refs": [
    {
      "module": "xarray",
      "version": "0.17.0",
      "kind": "module",
      "path": "xarray.plot.plot.line"
    },
    {
      "module": "xarray",
      "version": "0.17.0",
      "kind": "module",
      "path": "xarray.plot.plot.pcolormesh"
    },
    {
      "module": "xarray",
      "version": "0.17.0",
      "kind": "module",
      "path": "xarray.plot.plot.hist"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters"
  ],
  "item_file": "/Users/bussonniermatthias/miniconda3/lib/python3.8/site-packages/xarray/plot/plot.py",
  "item_line": 113,
  "item_type": "<class 'function'>",
  "aliases": [
    "xarray.plot.plot"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "0.17.0",
  "signature": "plot(darray, row=None, col=None, col_wrap=None, ax=None, hue=None, rtol=0.01, subplot_kws=None, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "xarray.plot.plot.plot",
  "arbitrary": []
}