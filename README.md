* LoopedList

returns any index as if it's infinite

```py
lst = LoopedList("Red", "Green", "Blue")
lst[20:25]

# ['Blue', 'Red', 'Green', 'Blue', 'Red']
```

* Headers

dict subclass for handling headers that might be different case or encoded

```py
headers = Headers({b"Content-Type": b"text/plain"})
headers["content-type"]

# text/plain
```

* get_first(**key**, obj)

returns the value of the first **key** found anywhere in a big json loaded object

```py
obj = """
{
    "a": {
        "b": [
            {
                "xyz": true
            },
            {
                "xyz": false
            }
        ]
    }
}
"""

get_first("xyz", json.loads(obj))

# True
```
