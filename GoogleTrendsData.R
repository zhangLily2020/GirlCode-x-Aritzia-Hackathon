library(tidyverse)
library(repr)
library(tidymodels)

raw_Gtrend <- read_csv("vis2_gtrends_data.csv")

gtrend_by_month <- raw_Gtrend %>% 
    group_by(month = lubridate::floor_date(date, 'month')) %>%
    summarize_all(mean)





most_trendy_item_by_month <- select(gtrend_by_month, 1,3:29) 

most_trendy_item_by_month$ most_trendy_item <- 
colnames(most_trendy_item_by_month)[apply(most_trendy_item_by_month,1,which.max)]

most_trendy_color_by_month <- select(gtrend_by_month, 1,30:39) 

most_trendy_color_by_month$ most_trendy_color <- 
colnames(most_trendy_color_by_month)[apply(most_trendy_color_by_month,1,which.max)]

most_trendy_material_by_month <- select(gtrend_by_month, 1,40:98) 

most_trendy_material_by_month$ most_trendy_material <- 
colnames(most_trendy_material_by_month)[apply(most_trendy_material_by_month,1,which.max)]

most_trendy_1 <- most_trendy_item_by_month %>% select(1,most_trendy_item)

most_trendy_2 <- most_trendy_color_by_month %>% select(most_trendy_color)

most_trendy_3 <- most_trendy_material_by_month %>% select(most_trendy_material)

most_trendy_temp <- cbind(most_trendy_1,most_trendy_2)

most_trendy <- cbind(most_trendy_temp, most_trendy_3)

write.csv(most_trendy,file='most_trendy.csv', row.names=TRUE)