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
                  "value": "Returns the factors of the polar decomposition  "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "u",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "u"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " and "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "p",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "p"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " such that "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "a = up"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " (if "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "side",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "side"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is \"right\") or "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "a = pu"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " (if "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "side",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "side"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is \"left\"), where "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "p",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "p"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is positive semidefinite. Depending on the shape of "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "a",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "a"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", either the rows or columns of "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "u",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "u"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " are orthonormal. When "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "a",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "a"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is a square array, "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "u",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "u"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is a square unitary array. When "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "a",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "a"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is not square, the \"canonical polar decomposition\"  is computed."
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
            "param": "a",
            "type_": "(m, n) array_like",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The array to be factored."
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
            "param": "side",
            "type_": "{'left', 'right'}, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Determines whether a right or left polar decomposition is computed. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "side",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "side"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is \"right\", then "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "a = up"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ".  If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "side",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "side"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is \"left\",  then "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "a = pu"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ".  The default is \"right\"."
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "u",
            "type_": "(m, n) ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "a",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "a"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is square, then "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "u",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "u"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is unitary. If m > n, then the columns of "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "a",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "a"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are orthonormal, and if m < n, then the rows of "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "u",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "u"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are orthonormal."
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
            "param": "p",
            "type_": "ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Link",
                      "data": {
                        "value": "p",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "p"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is Hermitian positive semidefinite. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "a",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "a"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is nonsingular, "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "p",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "p"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is positive definite. The shape of "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "p",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "p"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is (n, n) or (m, m), depending on whether "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "side",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "side"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is \"right\" or \"left\", respectively."
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
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Compute the polar decomposition."
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
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.sparse.linalg"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.linalg._decomp_polar.polar"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.ndarray"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.array"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "References",
    "Examples"
  ],
  "item_file": "/scipy/linalg/_decomp_polar.py",
  "item_line": 8,
  "item_type": "<class 'function'>",
  "aliases": [
    "scipy.signal.lti_conversion.linalg.polar"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "kn",
              "link": {
                "type": "str",
                "data": "from"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "nn",
              "link": {
                "type": "Link",
                "data": {
                  "value": "scipy",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "nn",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "nn",
              "link": {
                "type": "Link",
                "data": {
                  "value": "linalg",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse.linalg"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "kn",
              "link": {
                "type": "str",
                "data": "import"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "polar",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg._decomp_polar.polar"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "a",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "array",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.array"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "1"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "-"
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "1"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "2"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "4"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "polar",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg._decomp_polar.polar"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "a",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            }
          ],
          "out": "array([[ 0.85749293, -0.51449576],\n       [ 0.51449576,  0.85749293]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            }
          ],
          "out": "array([[ 1.88648444,  1.2004901 ],\n       [ 1.2004901 ,  3.94446746]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "A non-square example, with m < n:"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "b",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "array",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.array"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "mf",
              "link": {
                "type": "str",
                "data": "0.5"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "1"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "2"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "["
              }
            },
            {
              "type": "mf",
              "link": {
                "type": "str",
                "data": "1.5"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "3"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "4"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "]"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "polar",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg._decomp_polar.polar"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "b",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            }
          ],
          "out": "array([[-0.21196618, -0.42393237,  0.88054056],\n       [ 0.39378971,  0.78757942,  0.4739708 ]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            }
          ],
          "out": "array([[ 0.48470147,  0.96940295,  1.15122648],\n       [ 0.96940295,  1.9388059 ,  2.30245295],\n       [ 1.15122648,  2.30245295,  3.65696431]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "dot"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "   "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# Verify the decomposition."
              }
            }
          ],
          "out": "array([[ 0.5,  1. ,  2. ],\n       [ 1.5,  3. ,  4. ]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "dot"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "T"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "   "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# The rows of u are orthonormal."
              }
            }
          ],
          "out": "array([[  1.00000000e+00,  -2.07353665e-17],\n       [ -2.07353665e-17,   1.00000000e+00]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Another non-square example, with m > n:"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "c"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "b",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "T"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "polar",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.linalg._decomp_polar.polar"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "c"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            }
          ],
          "out": "array([[-0.21196618,  0.39378971],\n       [-0.42393237,  0.78757942],\n       [ 0.88054056,  0.4739708 ]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            }
          ],
          "out": "array([[ 1.23116567,  1.93241587],\n       [ 1.93241587,  4.84930602]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "dot"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "p"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "   "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# Verify the decomposition."
              }
            }
          ],
          "out": "array([[ 0.5,  1.5],\n       [ 1. ,  3. ],\n       [ 2. ,  4. ]])",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "T"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "dot"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "u"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "  "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# The columns of u are orthonormal."
              }
            }
          ],
          "out": "array([[  1.00000000e+00,  -1.26363763e-16],\n       [ -1.26363763e-16,   1.00000000e+00]])",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "1.7.1",
  "signature": "polar(a, side='right')",
  "references": null,
  "logo": "logo.png",
  "qa": "scipy.linalg._decomp_polar.polar",
  "arbitrary": []
}