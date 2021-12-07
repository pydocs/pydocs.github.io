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
                  "value": "Arrays sometimes contain invalid or missing data.  When doing operations on such arrays, we wish to suppress invalid values, which is the purpose masked arrays fulfill (an example of typical use is given below)."
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
                  "value": "For example, examine the following array:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])",
                  "_number": 0,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "When we try to calculate the mean of the data, the result is undetermined:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> np.mean(x)",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "nan",
                  "_number": 1,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The mean is calculated using roughly "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "np.sum(x)/len(x)"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", but since any number added to "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "  produces "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", this doesn't work.  Enter masked arrays:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> m = np.ma.masked_array(x, np.isnan(x))",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": ">>> m",
                  "_number": 1,
                  "_offset": 0
                },
                {
                  "_line": "masked_array(data = [2.0 1.0 3.0 -- 5.0 2.0 3.0 --],",
                  "_number": 2,
                  "_offset": 0
                },
                {
                  "_line": "      mask = [False False False  True False False False  True],",
                  "_number": 3,
                  "_offset": 0
                },
                {
                  "_line": "      fill_value=1e+20)",
                  "_number": 4,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Here, we construct a masked array that suppress all "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " values.  We may now proceed to calculate the mean of the other values:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> np.mean(m)",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "2.6666666666666665",
                  "_number": 1,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "BlockDirective",
          "data": {
            "directive_name": "moduleauthor",
            "args0": [],
            "inner": {
              "inline": [
                {
                  "type": "Words",
                  "data": {
                    "value": "Pierre Gerard - Marchant "
                  }
                }
              ],
              "inner": []
            }
          }
        },
        {
          "type": "BlockDirective",
          "data": {
            "directive_name": "moduleauthor",
            "args0": [],
            "inner": {
              "inline": [
                {
                  "type": "Words",
                  "data": {
                    "value": "Jarrod Millman "
                  }
                }
              ],
              "inner": []
            }
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
      "children": [],
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
      "children": [],
      "title": "Masked Arrays"
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
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary"
  ],
  "item_file": "/numpy/ma/__init__.py",
  "item_line": 0,
  "item_type": "<class 'module'>",
  "aliases": [
    "numpy.ma"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "1.21.3",
  "signature": null,
  "references": null,
  "logo": "logo.png",
  "qa": "numpy.ma",
  "arbitrary": [
    {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Arrays sometimes contain invalid or missing data.  When doing operations on such arrays, we wish to suppress invalid values, which is the purpose masked arrays fulfill (an example of typical use is given below)."
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
                  "value": "For example, examine the following array:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])",
                  "_number": 0,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "When we try to calculate the mean of the data, the result is undetermined:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> np.mean(x)",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "nan",
                  "_number": 1,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The mean is calculated using roughly "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "np.sum(x)/len(x)"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", but since any number added to "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "  produces "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", this doesn't work.  Enter masked arrays:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> m = np.ma.masked_array(x, np.isnan(x))",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": ">>> m",
                  "_number": 1,
                  "_offset": 0
                },
                {
                  "_line": "masked_array(data = [2.0 1.0 3.0 -- 5.0 2.0 3.0 --],",
                  "_number": 2,
                  "_offset": 0
                },
                {
                  "_line": "      mask = [False False False  True False False False  True],",
                  "_number": 3,
                  "_offset": 0
                },
                {
                  "_line": "      fill_value=1e+20)",
                  "_number": 4,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Here, we construct a masked array that suppress all "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "NaN"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " values.  We may now proceed to calculate the mean of the other values:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ">>> np.mean(m)",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "2.6666666666666665",
                  "_number": 1,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "BlockDirective",
          "data": {
            "directive_name": "moduleauthor",
            "args0": [],
            "inner": {
              "inline": [
                {
                  "type": "Words",
                  "data": {
                    "value": "Pierre Gerard - Marchant "
                  }
                }
              ],
              "inner": []
            }
          }
        },
        {
          "type": "BlockDirective",
          "data": {
            "directive_name": "moduleauthor",
            "args0": [],
            "inner": {
              "inline": [
                {
                  "type": "Words",
                  "data": {
                    "value": "Jarrod Millman "
                  }
                }
              ],
              "inner": []
            }
          }
        }
      ],
      "title": "Masked Arrays"
    }
  ]
}