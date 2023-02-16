setwd("/Users/adityaved/Downloads")
library(readxl)
df1 = read_excel("dac_test.xlsx")
df_size = df1$`Size of List (n)`
no_of_inputs_vec = unlist(df_size)
vec_dac = unlist(df1$`Time using DAC`)
vec_iterative = unlist(df1$`Time using Iterative`)


plot(no_of_inputs_vec,vec_dac, type = "o", col = "red")
lines(no_of_inputs_vec,vec_iterative, type = "o", col = "blue")