#!/usr/bin/env python3


import re

def clean_sites(input_text):

    tupla = re.findall(r"[a-zA-Z][a-zA-Z]\d\d\d\d\d", input_text)
    return tupla


def link_maker(raw_text):

    tupla = clean_sites(raw_text)

    all_init = "http://chancani.claro.amx:5601/s/amdocs/app/dashboards#/view/534d7f00-af34-11eb-9a05-75834ff0e051?_g=(filters:!(),refreshInterval:(pause:!f,value:180000),time:(from:now-24h,to:now))&_a=(description:'',filters:!(('$state':(store:appState),meta:(alias:!n,controlledBy:'1625163915808',disabled:!f,index:cfdee810-ae9e-11eb-9a05-75834ff0e051,key:location.name,negate:!f,params:"

    all_end = ",fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!f),query:(language:kuery,query:''),tags:!(),timeRestore:!f,title:'UC37%20-%20vista%20detallada',viewMode:view)"

    case_1_1 = "(query:"
    case_1_2 = "),type:phrase),query:(match_phrase:(location.name:"
    case_1_3 = "))))"

    case_more_1 = 'type:phrases,value:'
    case_more_2 = ',query:(bool:(minimum_should_match:1,should:!('
    case_more_loop_1 = ['(match_phrase:(location.name:']
    case_more_loop_close = ')))))'



    if len(tupla) == 1:
        site = tupla[0]
        final_link = all_init + case_1_1 + site + case_1_2 + site + case_1_3 + all_end

        return(final_link)
    else:

        #print(tupla)

        use_in_loop_1 = '!('
        for sites in tupla:
            use_in_loop_1 = use_in_loop_1 + sites + ','
        use_in_loop_1 = f"{use_in_loop_1[0: -1]}"
        use_in_loop_1 = use_in_loop_1 + '),'


        use_in_loop_2 = "'"

        for sites in tupla:
            use_in_loop_2 = use_in_loop_2 + sites + ',%20'
            case_more_loop_1.append(sites)
            case_more_loop_1.append('))')
            case_more_loop_1.append(',(match_phrase:(location.name:')


        case_more_loop_1.pop()
        loop_1 = ''.join(case_more_loop_1)

        use_in_loop_2 = f"{use_in_loop_2[0: -4]}"
        use_in_loop_2 = use_in_loop_2 + "')"


        final_link = all_init + use_in_loop_1
        '''
        print(all_init)
        print(use_in_loop_1)
        print(case_more_1)
        print(use_in_loop_2)
        print(case_more_2)
        print(loop_1)
        print(case_1_3)
        print(all_end)
        '''
        final_link = all_init + use_in_loop_1 + case_more_1 + use_in_loop_2 + case_more_2 + loop_1 + case_more_loop_close + all_end

    return(final_link)







a = link_maker(':!(CO01178,FO00035,FO00032),typ')
print(a)
