# Amro-Zayed-s-Laboratory-YorkU
MailMerge 

mergeEmailDL.py

mergeEmailDL.py is used to merge duplicated emails in an excel spread sheet into distinct ones and merge all their associated records without losing any record.

To use this program

Step 1, export emails and their associated records from the excel spread sheet out to a .txt formate file. Give it any name such as "mergList.txt"

Step2, move the "mergList.txt" under the same directory of this program.

Step3, run ./mergeEmailDL.py mergList.txt > mergedfile.txt 

Note the mergedfile.txt is where you save the final results onto. You can give any name to this file.

*If you only want to view the results, you can just run ./mergeEmailDL.py mergList.txt

Once you have the dinstinct emails list(mergedfile.txt), use import it to a excel sheet.
Copy and paste the data in the excel sheet to the mailMerge template in BeeServer/mailDistributionListSurvery/emailMergdListSurvery.xlsx (make sure you clear the previous records or make a copy for old records)

*In order to use the MailMerge function, you have to familiar with the MailMerge add-on which is free on Google Sheet.
Watch this tutorial for your first time to use MailMerge, http://www.labnol.org/software/mail-merge-with-gmail/13289/

From emailMergdListSurvery.xlsx(in Google Sheets formate), select "Add-ons" -> "Mail Merge with attachements" ->"Config Mail Merge"->Choose "Sender's Email Address:" and fill in "Reply-to Address:"  -> select "Choose email Templates" -> locate the email draft(your template) from your gmail draft list-> Select "Run Mail Merge"
