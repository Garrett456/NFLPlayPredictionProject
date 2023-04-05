library(tidyverse)
library(lubridate)

data <- read.csv("/Users/garrett/Desktop/GitHub/NFLPlayPredictionProject/raw-data/nfl_games_pbp.csv")

data <- data %>%
  mutate(num = as.integer(gsub("\\D", "", yards_to_endzone)) ) %>%
  mutate(abbr = gsub("\\W", "", yards_to_endzone) ) %>%
  mutate(abbr = gsub("\\d", "", abbr) )

#unique(data$Abbreviation)
#unique(data$abbr)

# ARI, ARZ
# CLE, CLV
# BAL, BLT
# LA, LAR *
# HOU, HST

data <- data %>%
  mutate(abbr = str_replace( abbr, "ARZ", "ARI" ) ) %>%
  mutate(abbr = str_replace( abbr, "CLV", "CLE" ) ) %>%
  mutate(abbr = str_replace( abbr, "BLT", "BAL" ) ) %>%
  mutate(abbr = str_replace( abbr, "HST", "HOU" ) ) %>%
  mutate(Abbreviation = str_replace( Abbreviation, "LAR", "LA" ) )


data <- data %>%
  mutate( yards_to_endzone = ifelse(abbr == Abbreviation, 100 - num, num ) )

data <- data %>%
  select( -c('num', 'abbr') ) %>%
  rename( possession_abbr = Abbreviation )

#rename(data, c("possession_abbr" = "Abbreviation") )

data <- data %>%
  select( c('game', 'possession_team', 'possession_abbr', 'quarter',
            'time', 'shotgun', 'down', 'yards_to_first', 'yards_to_endzone', 'run_pass' ) )

data <- data %>%
  mutate( quarter = as.factor(quarter) ) %>%
  mutate( shotgun = as.factor(shotgun) ) %>%
  mutate( down = as.factor(down) ) %>%
  mutate( yards_to_endzone = as.integer(yards_to_endzone) ) %>%
  mutate( run_pass = as.factor(run_pass) )

# ifelse( grepl("^\\:"), paste0("0"+ time), time )

data <- data %>%
  mutate( time = ifelse(substr(time, 1, 1) == ":", paste0("0", time), time) )

str(data)

#write.csv(data, "/Users/garrett/Desktop/games_pbp.csv")

games_pbp <- data

usethis::use_data(games_pbp)







