Hi @tefra, thank you for this package! I use it very often to generate type hints for SOAP payloads.

The issue I encountered lately in one of my projects was, that when a WSDL references an equally-named XSD file, the generated "wsdl types" end up being overwritten by the "xsd types".
E.g. `path/SoapService.wsdl` references `path/SoapService.xsd`, running `xsdata path/SoapService.wsdl` will only generate a `generated/path/soap_service.py` file, equivalent to running `xsdata path/SoapService.xsd`.

What I propose is to raise an error so the user knows about this and provide a utility that will rename the files for them.

I work with local WSDLs, I don't know how xsdata handles this for remote URLs.

I've made [this repo](https://github.com/dsfaccini/xsdata-issues) for you to easily reproduce this behavior, the source for the WSDL/XSD files is in the README.

Thank you so much and let me know if you'd like me to make a pull request to implement this warning/fix.

Best regards,
David