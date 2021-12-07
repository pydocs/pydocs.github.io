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
                  "value": "Returns a sparse (m x n) matrix where the kth diagonal is all ones and everything else is zeros."
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
            "param": "m",
            "type_": "int",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Number of rows in the matrix."
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
            "param": "n",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Number of columns. Default: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "m",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "m"
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
                        "value": "Diagonal to place ones on. Default: 0 (main diagonal)."
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
                        "value": "Data type of the matrix."
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
            "param": "format",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Sparse format of the result, e.g., format=\"csr\", etc."
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
                  "value": "Sparse matrix with ones on diagonal"
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
      "path": "scipy.sparse.construct.eye"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.signedinteger"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.sparse"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Examples"
  ],
  "item_file": "/scipy/sparse/construct.py",
  "item_line": 219,
  "item_type": "<class 'function'>",
  "aliases": [
    "scipy.signal.filter_design.optimize._differentiable_functions.sps.eye"
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
                  "value": "sparse",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse"
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
                  "value": "sparse",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse"
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
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse.construct.eye"
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
                "data": ")"
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
                "data": "toarray"
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
          "out": "array([[ 1.,  0.,  0.],\n       [ 0.,  1.,  0.],\n       [ 0.,  0.,  1.]])",
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
                "type": "Link",
                "data": {
                  "value": "sparse",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse"
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
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.sparse.construct.eye"
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
                "data": "dtype"
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
                "type": "Link",
                "data": {
                  "value": "np",
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
                  "value": "int8",
                  "reference": {
                    "module": "numpy",
                    "version": "1.21.3",
                    "kind": "module",
                    "path": "numpy.signedinteger"
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
            }
          ],
          "out": "<3x3 sparse matrix of type '<class 'numpy.int8'>'\n    with 3 stored elements (1 diagonals) in DIAgonal format>",
          "ce_status": "execed"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "1.7.1",
  "signature": "eye(m, n=None, k=0, dtype=<class 'float'>, format=None)",
  "references": null,
  "logo": "logo.png",
  "qa": "scipy.sparse.construct.eye",
  "arbitrary": []
}