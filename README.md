# basicRouter
basic router method which returns the controller function name(s) based on route path

# Run
`cd to/dir/where/main.py`

`python3 main.py`

# About

### set path
set path --vs--> controller function

set( /home,home() ) --means set--> /home -> home()

e.g:
``` 
/home -> home()
/home/details -> details()
/home/1/profile -> profile(1)
/home/2/profile -> profile(2)
```


### get controller fn from path
```
get(/home)  --returns--> home()
```

also supports wild card

`get(/home/*/profile) --returns--> [ profile(1), profile(2) ] `

# LLD design

`https://drive.google.com/file/d/1yAJb5wJaE2yyJfKWKTSGc6U8FlhfrwLx/view?usp=sharing`
