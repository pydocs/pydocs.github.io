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
            "param": "None",
            "type_": "",
            "desc": []
          }
        }
      ],
      "title": null
    },
    "Raises": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "",
            "type_": "numpy.linalg.LinAlgError: Singular matrix",
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
                      "type": "Directive",
                      "data": {
                        "value": "self",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is singular."
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
    "Receives": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "ret",
            "type_": "matrix object",
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
                      "type": "Directive",
                      "data": {
                        "value": "self",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is non-singular, "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "ret",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "ret"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is such that "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "ret * self"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " == "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "self * ret"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " == "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "np.matrix(np.eye(self[0,:].size))"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " all return "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "True"
                        ]
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
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Returns the (multiplicative) inverse of invertible "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "self",
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
      "path": "numpy.matrix"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "Raises",
    "See Also",
    "Examples"
  ],
  "item_file": "/numpy/matrixlib/defmatrix.py",
  "item_line": 792,
  "item_type": "<class 'function'>",
  "aliases": [
    "numpy.matrix.getI"
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
                "data": "m"
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
                  "value": "matrix",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.matrix"
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
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "[1, 2; 3, 4]"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
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
                "data": ";"
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
                "data": "m"
              }
            }
          ],
          "out": "matrix([[1, 2],\n        [3, 4]])",
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
                "data": "m"
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
                "data": "getI"
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
                "data": ")"
              }
            }
          ],
          "out": "matrix([[-2. ,  1. ],\n        [ 1.5, -0.5]])",
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
                "data": "m"
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
                "data": "getI"
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
                "data": ")"
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
                "data": "*"
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
                "data": "m"
              }
            }
          ],
          "out": "matrix([[ 1.,  0.], # may vary\n        [ 0.,  1.]])",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "linalg.inv",
        "ref": "numpy.linalg.inv",
        "exists": true
      },
      "descriptions": [],
      "type": null
    }
  ],
  "version": "1.22.1",
  "signature": "I(self)",
  "references": null,
  "logo": "logo.png",
  "qa": "numpy.matrixlib.defmatrix.matrix.I",
  "arbitrary": []
}