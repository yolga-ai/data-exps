# data-exps
Data managing experiments and learnings. For education puposes. 



## do_data.py
File for generating big txt files with rows: id,amount, city:
id - sequence 
amount - random number 
city - randomly choosed capital from a list 

Use it for generate 1Gb or 10Gb txt file.


## process_data.py

File for extraacting data from big txt file and aggregating it with pandas. 


Time Results on data:

**1GB txt file**
> processing file 973.8mb
> ...time took: 3907 seconds
> agg and count data:
> ...time took: 5 seconds
> CPU memory used during session ~ 4-5GB

**23Mb txt file**
> processing file 22.6mb
> ...time took: 5 seconds
> agg and count data:
> ...time took: 0 seconds
> saving to agg.txt:
> ...time took: 0 seconds