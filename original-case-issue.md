Hi @tefra, 

Working on this same project I wanted to use originalCase for both the *Class names* and the *Field names*. The reason is, I already have a partial code base using the original names (in `PascalCase`) and mapping these existing functions to generated `snake_case` *Class* and *Field* names is a whole chore.

So I modiefied the xsdata init-config file to preserve the case and I got a recursion error on the last step of generation.
```xml
    <!-- <ClassName case="originalCase" safePrefix="type"/> -->
    <!-- <FieldName case="originalCase" safePrefix="value"/> -->
```
```
  File "C:\Users\dsfaccini\AppData\Local\Programs\Python\Python311\Lib\dataclasses.py", line 284, in __repr__
    return ('Field('
            ^^^^^^^^
  File "C:\Users\dsfaccini\AppData\Local\Programs\Python\Python311\Lib\typing.py", line 1643, in __repr__
    return f'typing.Optional[{_type_repr(args[0])}]'
                              ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\dsfaccini\AppData\Local\Programs\Python\Python311\Lib\typing.py", line 242, in _type_repr
    return repr(obj)
           ^^^^^^^^^
RecursionError: maximum recursion depth exceeded
```
I'm guessing the recursion error comes from the WSDL having the same name as the XSD? But I'm not sure about this.

You can try it by [cloning this repo](https://github.com/dsfaccini/xsdata-issues) and running the generate script.

Also, if you look at the generated module (generated/conn/signature_service_v7_5_6.py) you'll see the following on line 259

```python
    Context: Optional[Context] = Field(...
```

This messes up Pylance/Pyright, since it recognizes this as the field referencing itself.
`Variable not allowed in type expression *Pylance*(reportInvalidTypeForm)`
The correct generation in those cases should be 
```python
    Context: Optional['Context'] = Field(...
```

Let me know if you'd like me to put up a pull request to adjust this behavior! It would be helpful in that case if you could nudge me a bit on what file/s to look into.

Best regards,
David