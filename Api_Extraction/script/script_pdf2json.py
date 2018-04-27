from Api_Extraction.extraction import Extraction
import json
import glob
import codecs
import datefinder

extraction = Extraction('../../')

def extract_pdf2json(folder):
    for filename in glob.glob(folder+'/*.pdf'):
        if not filename.endswith('.pdf'):
            continue
        result = extraction.parse_cv(filename)
        print(filename)
        outfile = codecs.open(filename[:-4]+'.json','w','utf-8')
        outfile.write(json.dumps(result,ensure_ascii=False))
        outfile.close()
        print(result['person_details'])

def extract_pdf(pathfile):
    result = extraction.parse_cv(pathfile)
    print('Personal Detail')
    for item in result['person_details'].items():
        print(item)
    print('Education')
    for item in result['education'].items():
        print(item)

    print('Skill')
    for item in result['skills'].items():
        print(item)

    print('Experience')
    for item in result['experience']:
        print(item)

    print("Other")
    print(result['other'])
    result = json.dumps(result,ensure_ascii=False)
    return result

def show_cv_json(json_cv):
    person = json_cv.get('person_details',None)
    if person != None:
        print('\n---------------------------Personal details--------------------\n')
        for k,v in person.items():
            if v!= None:
                # if k=='birth_day':
                #     matches = datefinder.find_dates(v)
                #     for match in  matches:
                #         print('birth_day',match.date())
                #
                # else:
                print(k,':',v)

    education = json_cv.get('education',None)
    if education != None:
        print('\n-----------------------------Education---------------------------\n')
        for k, v in education.items():
            if v!= None and len(v)>0:
                print(k,':',v)

    skill = json_cv.get('skill',None)
    if skill!= None:
        print('\n------------------------Skill------------------------\n')
        for k, v in education.items():
            if v!= None and len(v)>0:
                print(k,':',v)

    experiences = json_cv.get('experience',None)
    if experiences!= None:
        print('\n----------------------------Experience------------------------\n')
        for experience in experiences:
            for k,v in experience.items():
                if v!= None and len(v)>0:
                    print(k,':',v)

if __name__ == "__main__":
    extraction = Extraction('../../')
    # extract_pdf2json('../../../../Machine Learning/ReadPDF/data/cv/en/done')
    result = extraction.parse_cv('../../../../Machine Learning/ReadPDF/data/cv/en/done/ITSOL_CV_IOS_ Ta Cuong.pdf')
    show_cv_json(result)
    # show_cv_json(extraction.parse_cv('../../../../Machine Learning/ReadPDF/data/cv/en/done/ITSOL_CV_IOS_ Ta Cuong.pdf'))
    # extract_pdf('../../../../Machine Learning/ReadPDF/data/cv/en/done/ITSOL_CV_IOS_ Ta Cuong.pdf')
    # extract_pdf('../../../../Machine Learning/ReadPDF/data/cv/vi/HR - Vu-Thi-Thu.pdf')
    # extract_pdf('../cv/pham_van_tien.docx')