library(plyr)
library(tidyverse)

path <- "/Users/garrett/Desktop/pbp_text_2/49ers_at_bears_2022_reg_1.txt"
path_2 <- "/Users/garrett/Desktop/pbp_text_2/bengals_at_cowboys_2022_reg_2.txt"
path_3 <- "/Users/garrett/Desktop/pbp_text_2/bills_at_dolphins_2022_reg_3.txt"

wrangle <- function(file_path){

  nfl_teams <- read.csv("/Users/garrett/Desktop/nfl_teams.csv")
  nfl_teams <- nfl_teams %>% select(Name, Abbreviation)
  
  lines <- readLines(file_path)
  
  
  pattern <- "First Quarter Play By Play"
  line_index <- grep(pattern, lines)
  
  if (length(line_index) > 0) {
    lines_2 <- lines[line_index:length(lines)]
  }
  head(lines_2, 25)
  
  
  df <- data.frame(game = character(0),
                   possession_team = character(0),
                   quarter = numeric(0),
                   time = character(0),
                   shotgun = character(0),
                   down = integer(0),
                   yards_to_first = integer(0),
                   yards_to_endzone = character(0),
                   run_pass = character(0))
  
  game_id_1 <- substring(file_path, 35)
  game_id <- substr(game_id_1, start = 1, stop = nchar(game_id_1) - 4)
  
  # Initialize the quarter variable
  quarter <- 1
  counter <- 0
  
  # Initialize the possession_team variable
  possession_team <- ""
  
  # Loop through each line
  for (line in lines_2) {
    
    # Update possession_team if line contains an NFL team name
    for (team_name in nfl_teams$Name) {
      if (grepl(team_name, line)) {
        possession_team <- team_name
        next
      }
    }
    #  || !grepl("^\\(:", line)
    # Only process lines that start with "(" then any digit
    if (!grepl("^\\(\\d", line) && !grepl("^\\(:", line)) {
      next
    }
    
    # Ignore lines containing "PENALTY"
    if (grepl("PENALTY", line)) {
      next
    }
    
    # Ignore lines containing "REVERSED"
    if (grepl("REVERSED", line)) {
      next
    }
    
    # Ignore lines containing "punts"
    if (grepl("punts", line)) {
      next
    }
    
    # Ignore lines containing "field goal"
    if (grepl("field goal", line)) {
      next
    }
    
    # Ignore lines containing "sacked"
    if (grepl("sacked", line)) {
      next
    }
    
    # Extract time from the line
    time <- gsub("^\\((\\d{0,2}:\\d{2})\\).*", "\\1", line)
    
    # Increment the counter for quarter
    counter <- counter + 1
    
    # Increment quarter if time is 15:00
    if (counter < 3){
      quarter <- 1
    } else if (time == "15:00") {
      quarter <- min(quarter + 1, 4)
    }
    
    # Check if "Shotgun" appears in the line
    shotgun <- ifelse(grepl("Shotgun", line), "yes", "no")
    
    # Check if "pass" appears in the line
    run_pass <- ifelse(grepl("pass", line), "pass", "run")
    
    # Extract down, yards_to_first, and yards_to_endzone from the line
    down <- as.integer(gsub(".*\\s(\\d+)-\\d+-[A-Z]+\\s\\d+.*$", "\\1", line))
    yards_to_first <- as.integer(gsub(".*\\s\\d+-(\\d+)-[A-Z]+\\s\\d+.*$", "\\1", line))
    yards_to_endzone <- gsub(".*\\s\\d+-\\d+(-[A-Z]+\\s\\d+).*$", "\\1", line)
    
    # Append the extracted information to the data frame
    df <- rbind(df, data.frame(game = game_id,
                               possession_team = possession_team,
                               quarter = quarter,
                               time = time,
                               shotgun = shotgun,
                               down = down,
                               yards_to_first = yards_to_first,
                               yards_to_endzone = yards_to_endzone,
                               run_pass = run_pass))
  }
  
  # merge data frames to get abbreviation column
  df <- inner_join(df, nfl_teams, by= c("possession_team"="Name"))
  
  # remove na values
  df <- na.omit(df)
  
  # create export path
  export_path <- paste("/Users/garrett/Desktop/pbp_csv/", game_id, sep="")
  export_path_1 <- paste(export_path, '.csv', sep="")
  
  # export df as a csv
  write.csv(df, export_path_1, row.names=FALSE)
  
  # return df
  return(df)
}

#test <- wrangle(path_2)


# loop through all files in folder
folder_path <- '/Users/garrett/Desktop/pbp_text_2'
folder_path_1 <- '/Users/garrett/Desktop/pbp_text_2/'

# List all files in the folder
all_files <- list.files(path = folder_path)

# Loop through each file
for (file in all_files) {
  # Check if the file has a .txt extension
  if (grepl("\\.txt$", file)) {
    
    # create file path
    file_path <- paste(folder_path_1, file, sep = '')
    
    # call wrangle function
    wrangle(file_path)
  }
}


# combine all csv in folder

folder_path_csv <- '/Users/garrett/Desktop/pbp_csv'
folder_path_csv_1 <- '/Users/garrett/Desktop/pbp_csv/'

# List all .csv files in the folder
csv_files <- list.files(path = folder_path_csv)

# Initialize an empty data frame to store the combined data
nfl_games_pbp <- data.frame()

# Loop through each .csv file
for (file in csv_files) {
  
  # create file path
  file_path <- paste(folder_path_csv_1, file, sep = '')
  
  # Read the .csv file
  temp_data <- read.csv(file_path)
  
  # Combine the data frame with the previous ones using rbind
  nfl_games_pbp <- rbind(nfl_games_pbp, temp_data)
}

# write data set to desktop
write.csv(nfl_games_pbp, "/Users/garrett/Desktop/nfl_games_pbp.csv", row.names=FALSE)







