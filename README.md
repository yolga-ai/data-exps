# data-exps
Data managing experiments and learnings. For education puposes. 



## [do_data.py](https://github.com/yolga-ai/data-exps/blob/main/do_data.py)
File for generating big txt files with rows: id,amount, city:
* id - sequence 
* amount - random number 
* city - randomly choosed capital from a list 

Use it for generate 1Gb or 10Gb txt file.


## [process_data.py](https://github.com/yolga-ai/data-exps/blob/main/process_data.py)
File for extraacting data from big txt file and aggregating it with pandas. 


Time Results on data:

File | Read file with .read_csv() | Agg and Count | Save with .to_csv()
------------ | ------------- | ------------- | -------------
** 22.6mb txt file** | 5 secs | 0 secs | 0 secs
** 973.8mb txt file** | 3907 secs | 5 secs | ? secs