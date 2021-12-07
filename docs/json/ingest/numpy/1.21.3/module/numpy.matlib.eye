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
            "param": "n",
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
                        "value": "Number of columns in the output, defaults to "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "n",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "n"
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
                        "value": "Index of the diagonal: 0 refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal."
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
            "type_": "dtype, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Data-type of the returned matrix."
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
            "type_": "matrix",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "A "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "n",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "n"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " x "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "M",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "M"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " matrix where all elements are equal to zero, except for the "
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
                  "value": "Return a matrix with ones on the diagonal and zeros elsewhere."
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
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.eye"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.matlib"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.dtype"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.testing._private.utils.import_nose"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Examples"
  ],
  "item_file": "/numpy/matlib.py",
  "item_line": 187,
  "item_type": "<class 'function'>",
  "aliases": [
    "numpy.matlib.eye"
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
                "type": "Link",
                "data": {
                  "value": "import",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
                    "kind": "module",
                    "path": "numpy.testing._private.utils.import_nose"
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
              "type": "nn",
              "link": {
                "type": "Link",
                "data": {
                  "value": "numpy",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
                    "kind": "module",
                    "path": "numpy"
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
                  "value": "matlib",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
                    "kind": "module",
                    "path": "numpy.matlib"
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
                  "value": "matlib",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
                    "kind": "module",
                    "path": "numpy.matlib"
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
                  "value": "eye",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
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
                    "version": "1.21.3",
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
                "data": "float"
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
          "out": "matrix([[0.,  1.,  0.],\n        [0.,  0.,  1.],\n        [0.,  0.,  0.]])",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [
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
                "value": "Square identity matrix."
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
        "name": "numpy.eye",
        "ref": "numpy.eye",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Equivalent array function."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "1.21.3",
  "signature": "eye(n, M=None, k=0, dtype=<class 'float'>, order='C')",
  "references": null,
  "logo": "logo.png",
  "qa": "numpy.matlib.eye",
  "arbitrary": []
}