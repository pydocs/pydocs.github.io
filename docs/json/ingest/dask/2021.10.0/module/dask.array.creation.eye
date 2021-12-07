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
            "param": "chunks",
            "type_": "int, str",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "How to chunk the array. Must be one of the following forms:"
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BulletList",
                "data": {
                  "value": [
                    {
                      "type": "Paragraph",
                      "data": {
                        "inline": [
                          {
                            "type": "Words",
                            "data": {
                              "value": "A blocksize like 1000."
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
                              "value": "A size in bytes, like \"100 MiB\" which will choose a uniform     block-like shape"
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
                              "value": "The word \"auto\" which acts like the above, but uses a configuration     value "
                            }
                          },
                          {
                            "type": "Verbatim",
                            "data": {
                              "value": [
                                "array.chunk-size"
                              ]
                            }
                          },
                          {
                            "type": "Words",
                            "data": {
                              "value": " for the chunk size"
                            }
                          }
                        ],
                        "inner": []
                      }
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
            "type_": "Array of shape (N,M)",
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
                  "value": "Return a 2-D Array with ones on the diagonal and zeros elsewhere."
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
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns"
  ],
  "item_file": "/dask/array/creation.py",
  "item_line": 510,
  "item_type": "<class 'function'>",
  "aliases": [
    "dask.array.eye"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "2021.10.0",
  "signature": "eye(N, chunks='auto', M=None, k=0, dtype=<class 'float'>)",
  "references": null,
  "logo": "logo.png",
  "qa": "dask.array.creation.eye",
  "arbitrary": []
}