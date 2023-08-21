from datetime import datetime

from parse import Parse_Time


class TimeList:
    if datetime.today().isoweekday() != 6 or 7:
        st1_B = Parse_Time(9, 0)

        st2_in_B = Parse_Time(8, 0)

        st2_in_P = Parse_Time(8, 1)

        st3_in_B = Parse_Time(7, 0)

        st3_in_P = Parse_Time(7, 1)

        st4_in_B = Parse_Time(6, 0)

        st4_in_P = Parse_Time(6, 1)

        st5_in_B = Parse_Time(5, 0)

        st5_in_P = Parse_Time(5, 1)

        st6_in_B = Parse_Time(4, 0)

        st6_in_P = Parse_Time(4, 1)

        st7_in_B = Parse_Time(3, 0)

        st7_in_P = Parse_Time(3, 1)

        st8_in_B = Parse_Time(2, 0)

        st8_in_P = Parse_Time(2, 1)

        st9_P = Parse_Time(1, 0)
    else:
        st1_B = Parse_Time(9, 1)

        st2_in_B = Parse_Time(8, 2)

        st2_in_P = Parse_Time(8, 3)

        st3_in_B = Parse_Time(7, 2)

        st3_in_P = Parse_Time(7, 3)

        st4_in_B = Parse_Time(6, 2)

        st4_in_P = Parse_Time(6, 3)

        st5_in_B = Parse_Time(5, 2)

        st5_in_P = Parse_Time(5, 3)

        st6_in_B = Parse_Time(4, 2)

        st6_in_P = Parse_Time(4, 3)

        st7_in_B = Parse_Time(3, 2)

        st7_in_P = Parse_Time(3, 3)

        st8_in_B = Parse_Time(2, 2)

        st8_in_P = Parse_Time(2, 3)

        st9_P = Parse_Time(1, 1)
