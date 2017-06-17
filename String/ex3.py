def get_char(sample_string):
        if len(sample_string) >= 2:
            print sample_string[0:2] + sample_string[-2:] 
        else:
            print "empty string"


get_char('koci')            
    