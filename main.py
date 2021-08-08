#!/usr/bin/env python

import os
import glob
import getopt
import sys
import pandas as pd


def main(argv):
   # set some defaults
   sheet_name = "Sheet1"
   separator = ","
   path = "./"
   match = "*.csv"
   outputfile = ""

   # read command line args
   try:
       opts, args = getopt.getopt(
           argv, "hp:m:o:n:s:", ["path=", "match=", "output=", "name=", "separator="]
       )
   except getopt.GetoptError:
       print("main.py -p <path to files> -m <match pattern> -o <output file>")
       sys.exit(2)

   # over write the defaults with command line args (if set)
   for opt, arg in opts:
       if opt == "-h":
           print("main.py -p <path to files> -m <match pattern> -o <output file>")
           sys.exit()
       elif opt in ("-p", "--path"):
           path = arg
       elif opt in ("-o", "--output"):
           outputfile = arg
       elif opt in ("-m", "--match"):
           match = arg
       elif opt in ("-n", "--name"):
           sheet_name = arg
       elif opt in ("-s", "--separator"):
           separator = arg
   
   # scan for files in the given path matching the glob
   all_file_paths = glob.glob(os.path.join(path, match))

   # declare an array for pandas data frames, then read each csv in as a data frame
   all_data_frames = []
   for f in all_file_paths:
       df = pd.read_csv(f, sep=separator)
       df["file"] = f.split("/")[-1]
       all_data_frames.append(df)
   
   # combine all the data frames from the array
   merged_data_frame = pd.concat(all_data_frames, ignore_index=True)

   # log out the results for fun (best to comment this out)
   # print(merged_data_frame)

   # write out the concatenated results to an excel file
   merged_data_frame.to_excel(outputfile, sheet_name=sheet_name)


if __name__ == "__main__":
    main(sys.argv[1:])
