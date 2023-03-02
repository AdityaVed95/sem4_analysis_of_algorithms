setwd("/Users/adityaved/prj_ws/git_hub_repos/sem4_analysis_of_algorithms/AOA_Labs/Lab3_merge_quick_sort")

library(readxl)
df1 = read_excel("merge_vs_quick_sort_analyse.xlsx")

df_input_size = df1$`input size`
no_of_inputs_vec = unlist(df_input_size)


vec_merge = unlist(df1$`merge`)
vec_quick = unlist(df1$`quick`)

plot(no_of_inputs_vec,vec_merge, type = "o", col = "red")
lines(no_of_inputs_vec,vec_quick, type = "o", col = "blue")