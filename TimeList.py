from datetime import datetime

from parse import Parse_Time


class TimeList:
    if datetime.today().isoweekday() != 6 or 7:
        st1_B = Parse_Time(9)[0].text.replace(' ', '').replace(',', '').split(';')

        st2_in_B = Parse_Time(8)[0].text.replace(' ', '').replace(',', '').split(';')

        st2_in_P = Parse_Time(8)[1].text.replace(' ', '').replace(',', '').split(';')

        st3_in_B = Parse_Time(7)[0].text.replace(' ', '').replace(',', '').split(';')

        st3_in_P = Parse_Time(7)[1].text.replace(' ', '').replace(',', '').split(';')

        st4_in_B = Parse_Time(6)[0].text.replace(' ', '').replace(',', '').split(';')

        st4_in_P = Parse_Time(6)[1].text.replace(' ', '').replace(',', '').split(';')

        st5_in_B = Parse_Time(5)[0].text.replace(' ', '').replace(',', '').split(';')

        st5_in_P = Parse_Time(5)[1].text.replace(' ', '').replace(',', '').split(';')

        st6_in_B = Parse_Time(4)[0].text.replace(' ', '').replace(',', '').split(';')

        st6_in_P = Parse_Time(4)[1].text.replace(' ', '').replace(',', '').split(';')

        st7_in_B = Parse_Time(3)[0].text.replace(' ', '').replace(',', '').split(';')

        st7_in_P = Parse_Time(3)[1].text.replace(' ', '').replace(',', '').split(';')

        st8_in_B = Parse_Time(2)[0].text.replace(' ', '').replace(',', '').split(';')

        st8_in_P = Parse_Time(2)[1].text.replace(' ', '').replace(',', '').split(';')

        st9_P = Parse_Time(1)[0].text.replace(' ', '').replace(',', '').split(';')
    else:
        st1_B = Parse_Time(9)[1].text.replace(' ', '').replace(',', '').split(';')

        st2_in_B = Parse_Time(8)[2].text.replace(' ', '').replace(',', '').split(';')

        st2_in_P = Parse_Time(8)[3].text.replace(' ', '').replace(',', '').split(';')

        st3_in_B = Parse_Time(7)[2].text.replace(' ', '').replace(',', '').split(';')

        st3_in_P = Parse_Time(7)[3].text.replace(' ', '').replace(',', '').split(';')

        st4_in_B = Parse_Time(6)[2].text.replace(' ', '').replace(',', '').split(';')

        st4_in_P = Parse_Time(6)[3].text.replace(' ', '').replace(',', '').split(';')

        st5_in_B = Parse_Time(5)[2].text.replace(' ', '').replace(',', '').split(';')

        st5_in_P = Parse_Time(5)[3].text.replace(' ', '').replace(',', '').split(';')

        st6_in_B = Parse_Time(4)[2].text.replace(' ', '').replace(',', '').split(';')

        st6_in_P = Parse_Time(4)[3].text.replace(' ', '').replace(',', '').split(';')

        st7_in_B = Parse_Time(3)[2].text.replace(' ', '').replace(',', '').split(';')

        st7_in_P = Parse_Time(3)[3].text.replace(' ', '').replace(',', '').split(';')

        st8_in_B = Parse_Time(2)[2].text.replace(' ', '').replace(',', '').split(';')

        st8_in_P = Parse_Time(2)[3].text.replace(' ', '').replace(',', '').split(';')

        st9_P = Parse_Time(1)[1].text.replace(' ', '').replace(',', '').split(';')
