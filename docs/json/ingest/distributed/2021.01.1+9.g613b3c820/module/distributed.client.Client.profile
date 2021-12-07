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
                  "value": "Collect statistical profiling information about recent work"
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
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "key",
            "type_": "str",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Key prefix to select, this is typically a function name like 'inc' Leave as None to collect all data"
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
            "param": "start",
            "type_": "time",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "stop",
            "type_": "time",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "workers",
            "type_": "list",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "List of workers to restrict profile information"
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
            "param": "server",
            "type_": "bool",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If true, return the profile of the worker's administrative thread rather than the worker threads. This is useful when profiling Dask itself, rather than user code."
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
            "param": "scheduler",
            "type_": "bool",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If true, return the profile information from the scheduler's administrative thread rather than the workers. This is useful when profiling Dask's scheduling itself."
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
            "param": "plot",
            "type_": "boolean or string",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether or not to return a plot object"
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
            "param": "filename",
            "type_": "str",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Filename to save the plot"
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
      "module": "distributed",
      "version": "2021.01.1+9.g613b3c820",
      "kind": "module",
      "path": "distributed.profile"
    },
    {
      "module": "distributed",
      "version": "2021.01.1+9.g613b3c820",
      "kind": "module",
      "path": "distributed.client"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Examples"
  ],
  "item_file": "/Users/bussonniermatthias/dev/distributed/distributed/client.py",
  "item_line": 3311,
  "item_type": "<class 'function'>",
  "aliases": [
    "distributed.Client.profile"
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
                "type": "Link",
                "data": {
                  "value": "client",
                  "reference": {
                    "module": "distributed",
                    "version": "2021.01.1+9.g613b3c820",
                    "kind": "module",
                    "path": "distributed.client"
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
                  "value": "profile",
                  "reference": {
                    "module": "distributed",
                    "version": "2021.01.1+9.g613b3c820",
                    "kind": "module",
                    "path": "distributed.profile"
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
                "data": "# call on collections"
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
                  "value": "client",
                  "reference": {
                    "module": "distributed",
                    "version": "2021.01.1+9.g613b3c820",
                    "kind": "module",
                    "path": "distributed.client"
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
                  "value": "profile",
                  "reference": {
                    "module": "distributed",
                    "version": "2021.01.1+9.g613b3c820",
                    "kind": "module",
                    "path": "distributed.profile"
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
                "data": "filename"
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
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "dask-profile.html"
              }
            },
            {
              "type": "s2",
              "link": {
                "type": "str",
                "data": "\""
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
                "data": "# save to html file"
              }
            }
          ],
          "out": "",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "2021.01.1+9.g613b3c820",
  "signature": "profile(self, key=None, start=None, stop=None, workers=None, merge_workers=True, plot=False, filename=None, server=False, scheduler=False)",
  "references": null,
  "logo": "logo.png",
  "qa": "distributed.client.Client.profile",
  "arbitrary": []
}