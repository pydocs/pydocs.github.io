{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
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
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "N",
            "type_": "int",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Number of rows in the output."
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
            "param": "M",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Number of columns in the output. If None, defaults to "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "N",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "N"
                        },
                        "kind": "local",
                        "exists": true
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
        },
        {
          "type": "Param",
          "data": {
            "param": "k",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal."
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
            "param": "dtype",
            "type_": "data-type, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Data-type of the returned array."
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
            "param": "order",
            "type_": "{'C', 'F'}, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Admonition",
                "data": {
                  "kind": "versionadded",
                  "title": "TODO",
                  "children": [
                    {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "1.14.0 "
                          }
                        }
                      ],
                      "inner": []
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "like",
            "type_": "array_like",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "like"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " supports the "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "__array_function__"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Admonition",
                "data": {
                  "kind": "versionadded",
                  "title": "TODO",
                  "children": [
                    {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "1.20.0 "
                          }
                        }
                      ],
                      "inner": []
                    }
                  ]
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
            "param": "I",
            "type_": "ndarray of shape (N,M)",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "An array where all elements are equal to zero, except for the "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "k",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "k"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "-th diagonal, whose values are equal to one."
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
                  "value": "Return a 2-D array with ones on the diagonal and zeros elsewhere."
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
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.dtype"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.eye"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Examples"
  ],
  "item_file": "/numpy/lib/twodim_base.py",
  "item_line": 161,
  "item_type": "<class 'function'>",
  "aliases": [
    "numpy.eye",
    "numpy.lib.twodim_base._eye_with_like",
    "numpy.lib.twodim_base.eye"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "np"
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
                  "value": "eye",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.eye"
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
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "dtype",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.dtype"
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
                "data": "="
              }
            },
            {
              "type": "nb",
              "link": {
                "type": "str",
                "data": "int"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "array([[1, 0],\n       [0, 1]])",
          "ce_status": "execed"
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
                "data": "np"
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
                  "value": "eye",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.eye"
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
              "type": "",
              "link": {
                "type": "str",
                "data": "k"
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
                "data": ")"
              }
            }
          ],
          "out": "array([[0.,  1.,  0.],\n       [0.,  0.,  1.],\n       [0.,  0.,  0.]])",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "diag",
        "ref": "numpy.diag",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "diagonal 2-D array from a 1-D array specified by the user."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "identity",
        "ref": "numpy.identity",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "(almost) equivalent function"
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "1.22.1",
  "signature": "eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)",
  "references": null,
  "logo": "logo.png",
  "qa": "numpy.eye",
  "arbitrary": []
}