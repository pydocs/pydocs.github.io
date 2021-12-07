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
                  "value": "Type variable."
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
                  "value": "Usage::"
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
                  "_line": "  T = TypeVar('T')  # Can be anything",
                  "_number": 2,
                  "_offset": 2
                },
                {
                  "_line": "  A = TypeVar('A', str, bytes)  # Must be str or bytes",
                  "_number": 3,
                  "_offset": 2
                },
                {
                  "_line": "",
                  "_number": 4,
                  "_offset": 2
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
                  "value": "Type variables exist primarily for the benefit of static type checkers.  They serve as the parameters for generic types as well as for generic function definitions.  See class Generic for more information on generic types.  Generic functions work as follows:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "DefList",
          "data": {
            "children": [
              {
                "lines": {
                  "_lines": [
                    {
                      "_line": "  def repeat(x: T, n: int) -> List[T]:",
                      "_number": 10,
                      "_offset": 2
                    }
                  ]
                },
                "wh": {
                  "_lines": []
                },
                "ind": {
                  "_lines": [
                    {
                      "_line": "      '''Return a list containing n references to x.'''",
                      "_number": 11,
                      "_offset": 6
                    },
                    {
                      "_line": "      return [x]*n",
                      "_number": 12,
                      "_offset": 6
                    },
                    {
                      "_line": "",
                      "_number": 13,
                      "_offset": 6
                    }
                  ]
                },
                "dt": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "def repeat(x: T, n: int) -> List[T]:"
                      }
                    }
                  ],
                  "inner": []
                },
                "dd": [
                  {
                    "type": "Paragraph",
                    "data": {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "'''Return a list containing n references to x.''' return [x]*n "
                          }
                        }
                      ],
                      "inner": []
                    }
                  }
                ]
              },
              {
                "lines": {
                  "_lines": [
                    {
                      "_line": "  def longest(x: A, y: A) -> A:",
                      "_number": 14,
                      "_offset": 2
                    }
                  ]
                },
                "wh": {
                  "_lines": []
                },
                "ind": {
                  "_lines": [
                    {
                      "_line": "      '''Return the longest of two strings.'''",
                      "_number": 15,
                      "_offset": 6
                    },
                    {
                      "_line": "      return x if len(x) >= len(y) else y",
                      "_number": 16,
                      "_offset": 6
                    },
                    {
                      "_line": "",
                      "_number": 17,
                      "_offset": 6
                    }
                  ]
                },
                "dt": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "def longest(x: A, y: A) -> A:"
                      }
                    }
                  ],
                  "inner": []
                },
                "dd": [
                  {
                    "type": "Paragraph",
                    "data": {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "'''Return the longest of two strings.''' return x if len(x) >= len(y) else y "
                          }
                        }
                      ],
                      "inner": []
                    }
                  }
                ]
              }
            ]
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes.  Also note that if the arguments are instances of some subclass of str, the return type is still plain str."
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
                  "value": "At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError."
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
                  "value": "Type variables defined with covariant=True or contravariant=True can be used to declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables."
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
                  "value": "Type variables can be introspected. e.g.:"
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
                  "value": "  T.__name__ == 'T'   T.__constraints__ == ()   T.__covariant__ == False   T.__contravariant__ = False   A.__constraints__ == (str, bytes)"
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
                  "value": "Note that only type variables defined in global scope can be pickled."
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
      "children": [],
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
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary"
  ],
  "item_file": null,
  "item_line": null,
  "item_type": null,
  "aliases": [
    "xarray.core.common.T"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "0.17.0",
  "signature": null,
  "references": null,
  "logo": "logo.png",
  "qa": "xarray.core.common.T",
  "arbitrary": []
}