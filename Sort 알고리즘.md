# Sort 알고리즘

- dict에서 key 기준 정렬, value 기준 정렬

  - ```python
    # sorted() 함수내에 
    # key=operator.itemgetter(0) key, 
    # key=operator.itemgetter(1) val
    
    # key 기준은 default가 key이므로 reversed(my_dict) 해줘도 ok
    
    import operator
    my_dict = {500:[1], 2100:[4]}
    sorted_key = sorted(my_dict, key=operator.itemgetter(0))
    sorted_val = sorted(my_dict, key=operator.itemgetter(1))
    ```

- 배열에서 원하는 인덱스의 값으로 정렬하고 싶을 때

  - ```python
    # sorted() 함수 내에 i는 원하는 인덱스 번호
    # key=lambda x: x[i] 
    
    student_tuples = [
         ('john', 'A', 15),
         ('jane', 'B', 12),
         ('dave', 'B', 10),
     ]
    sorted(student_tuples, key=lambda student: student[2])   
    # sort by age
    [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    ```

