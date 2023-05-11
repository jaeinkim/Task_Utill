# import java.io.*;
# import java.util.StringTokenizer;
#
# class Main{
#     public static void main(String[] argv) throws IOException {
#         BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
#         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
#         StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
#         int cnt = 0;
#         while(st.hasMoreTokens()){
#             System.out.println(st.nextToken());
#             cnt++;
#         }
#         bw.write("cnt = " + cnt);
#         bw.flush();
#         bw.close();
#     }
# }

#ResvSubCode
param_list = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
#ResvCallID
# param_list2 = ['11400', '11401', '11402', '11403', '11404', '11405', '11406', '11407', '11408', '11409', '11410', '11411', '11412', '11413', '11414', '11415']
## 23/6/9 금
param_list2 = ['14131' ,'14132' ,'14133' ,'14134' ,'14135' ,'14136' ,'14137' ,'14138' ,'14139' ,'14140' ,'14141' ,'14142', '14143', '14144', '14145', '14146']
#StartDate
# param_str1 = '2023-02-10'
param_str1 = '2023-06-09'
# param_str2 = '2023-02-12'
param_str2 = '2023-06-11'

merged_param_list = list(zip(param_list, param_list2))

for str1, str2 in merged_param_list:
    # print(f'''console.log(CFN_CallAjaxJson('/WebSite/Extension/RSV/RsvAjax.aspx', '{{"METHOD":"SetResvAnswer","URCODE":"212758","ResvSubCode":{str1},"ResvCalID":{str2},"StartDate": ''' )
    print(f'''console.log(CFN_CallAjaxJson('/WebSite/Extension/RSV/RsvAjax.aspx', '{{"METHOD":"SetResvAnswer","URCODE":"212758","ResvSubCode":{str1},"ResvCalID":{str2},"StartDate":"{param_str1}","StartTime":null,"EndDate":"{param_str2}","EndTime":null,"ResvToken": "'+Rsv.GetResvCalInfo_Chk({str1}, {str2}, '{param_str1}').token+'\\" ,"ItemCode1":"1205","ItemAnswer1":"8","ItemCode2":"1206","ItemAnswer2":"Y","ItemCode3":0,"ItemAnswer3":null,"ItemCode4":0,"ItemAnswer4":null,"ItemCode5":0,"ItemAnswer5":null,"ItemCode6":0,"ItemAnswer6":null,"ItemCode7":0,"ItemAnswer7":null,"ItemCode8":0,"ItemAnswer8":null,"ItemCode9":0,"ItemAnswer9":null,"ItemCode10":0,"ItemAnswer10":null}}', false, null));''')
    # print('hi')


