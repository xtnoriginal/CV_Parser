import logging

import spacy
from spacy.tokens import DocBin
import json
import util


def train() -> None:
    nlp = spacy.blank('en')

    train_data = util.read_json('dataset/modeldata/traindata.json')

    db = DocBin()
    for content in train_data:
        doc = nlp(content['content'])
        #print(content['content'])
        entities = []

        for annotation in content['annotation']:

            point = annotation['points'][0]
            labels = annotation['label']

            if not isinstance(labels, list):
                labels = [labels]

            for label in labels:
                start = point['start']
                end = point['end'] + 1
                span = doc.char_span(start, end, label=label)
                print(start, end, label, span)
                #print(content['content'][start : end] )
                print(doc.text[start: end])
                # ToDo debug on why the span is NONE

                if(span == None):
                    continue

                #print(span.label , label)

                entities.append(span)
                break
                #ToDo  debug the  reason why its giving a double entry span



        doc.ents = entities
        db.add(doc)

    db.to_disk('./train.spacy')


if __name__ == '__main__':
    train()



