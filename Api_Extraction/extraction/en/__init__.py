from .person_detail import *
from .education import *
from .project import *
from .skill import *


def extract_detail(texts, topics, cluster_obj):
    result = {}
    result['name'] = None
    result['birth_day'] = None
    result['sex'] = None
    result['address'] = None
    result['mail'] = None
    result['number'] = None
    result['text'] = []
    height_max = 0
    obj_name = None
    date_max = 2
    max_person_line = 5
    index = 0
    for text, topic, objs in zip(texts, topics, cluster_obj):
        if topic == 'personal_details':
            for obj in objs:
                index+=1
                if height_max < obj.y1-obj.y0 and len(obj.text.strip())>0 and obj.text.upper().strip().split()[0] not in profile_words:
                    height_max = obj.y1-obj.y0
                    obj_name = obj
                name = detect_name(text)
                if name != None:
                    result['name'] = name
                birth_day = rex_time.has_date(obj.text) #detect_year(obj.text)
                if birth_day>date_max:
                    result['birth_day'] = obj.text if obj.text.find(':')==-1 else obj.text.split(':')[-1]
                    date_max = birth_day
                sex = detect_sex(text)
                if sex != None:
                    result['sex'] = sex
                address = rex.detect_address(obj.text, '')
                if address != None:
                    result['address'] = address
                mail = rex.detect_email(obj.text,'')
                if mail != None:
                    result['mail'] = mail
                number = detect_number(obj.text)
                if number != None:
                    result['number'] = number
            if result.get('address',None)==None:
                result['address'] = detect_address(text)
            result['text'].append(text)
        elif index<max_person_line:
            for obj in objs:
                index+=1
                if height_max < obj.y1-obj.y0 and obj.text.upper().strip().split()[0] not in profile_words:
                    height_max = obj.y1-obj.y0
                    obj_name = obj
                name = detect_name(obj.text)
                if name != None:
                    result['name'] = name
    if result['name'] == None and obj_name != None:
        result['name'] = detect_name('name '+obj_name.text.strip())
    return result



def extract_education(texts,topics):
    result = {}
    result['university'] = None
    result['cpa'] = None
    result['major'] = None
    result['language'] = []
    result['awards'] = []
    result['text'] =[]
    for text,topic in zip(texts,topics):
        if topic in ['education']:
            university = detect_university(text)
            if university != None:
                result['university']=university

            cpa = detect_cpa(text)
            if cpa != None:
                result['cpa']=cpa
            result['text'].append(text)
        if topic in ['language']:
            result['language'].append(text)
        if topic in ['awards']:
            result['awards'].append(text)
    return result



def extract_project(texts,topics,cluster_obj):
    result = []

    for text,topic,objs in zip(texts,topics,cluster_obj):
        if topic in ['experience']:
            project = {}
            project['company'] = None
            project['project'] = None
            project['position'] = None
            project['time'] = None
            project['skill'] = extract_skill([text],[topic])
            project['text'] = text
            result.append(project)
        else:
            for obj in objs:
                if obj.title in ['experience']:
                    project = {}
                    project['company'] = None
                    project['project'] = None
                    project['position'] = None
                    project['time'] = None
                    project['skill'] = extract_skill([text], [topic])
                    project['text'] = text
                    result.append(project)
                    break
    # result['company'] = list(set(result['company']))
    # result['project'] = list(set(result['project']))
    # result['position'] = list(set(result['position']))
    return result


def extract_other(texts,topics):
    result = {}
    result['objective'] = []

    for text,topic in zip(texts,topics):

        if topic in ['objective']:
            result['objective'].append(text)
    return result