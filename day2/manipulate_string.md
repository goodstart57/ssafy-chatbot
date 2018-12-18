# Manipulate String

## Index

1. Concatenation

2. Interpolation

3. 

## 1. Concatenation, 글자 합체

```python
# Code

"hello" + "JSLee"
```

```
# Output

hello JSLee
```

<br>

## 2. Interpolation : 글자 삽입

```python
# Code

name = "JSLee"
my_location = "seoul"
print(f"He is {name}, and he is in {my_location}")
```

```
# output

He is JSLee, and he is in seoul
```

<br>

```python
# Code

print(f"He is {name}, and he is in {my_location}".format(name = "JSLee", my_location = "seoul"))```

```
# output

He is JSLee, and he is in seoul
```

<br>

```python
# Code

print("He is {0}, and he is in {1}".format("JSLee", "seoul"))
```

```
# output

He is JSLee, and he is in seoul
```

## 3. Slicing : 글자 자르기

```python
# Code

greeting = "He is JSLee, and he is in seoul"
name = greeting[6:11]
print(greeting)
print(name)
```

```console
# Output

He is JSLee, and he is in seoul
JSLee
```
