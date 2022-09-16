library(dplyr)
library(tidyverse)
library(psych)
library(magrittr)
require(zoo)
require(lubridate)
PATH <- 'order_105773/order_105773_data.txt'

data <- read.csv(PATH, sep = ";")

data <- data %>%
  select(time, tre200dn, stn) %>%
  filter(stn == "MER") %>%
  select(-stn) %>%
  replace(.=="-", NA) %>%
  mutate_at(c('tre200dn'), as.numeric)

data$date <- as_date(data$time)
data <- data %>%
  select(-time) %>%
  select(date, tre200dn)

data_matrix <- as.matrix(data)

data_ts <- ts(data_matrix)

require(ggplot2)


