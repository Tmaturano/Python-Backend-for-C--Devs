## Collection

| C# | Python | 
|------|------|
| List<T> | list |
| HashSet<T> | set |
| Dictionary<TKey, TValue> | dict |
| Tuple | tuple |


## Python vs LINQ

### Select

- C#
```csharp
users.Select(x => x.Name)
```

- Python
```python
[user.name for user in users]
```

### Where

- C#
```csharp
users.Where(x => x.Active)
```

- Python
```python
[user for user in users if user.active]
```

### Any

- C#
```csharp
users.Any()
```

- Python
```python
any(users)
```

### Count

- C#
```csharp
users.Count()
```

- Python
```python
len(users)
```

### Contains

- C#
```csharp
users.Contains(user)
```

- Python
```python
user in users
```