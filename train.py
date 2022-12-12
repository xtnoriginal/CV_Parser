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
        entities = []

        for annotation in content['annotation']:

            point = annotation['points'][0]
            labels = annotation['label']

            if not isinstance(labels, list):
                labels = [labels]

            for label in labels:
                start = point['start']
                end = point['end']
                span = doc.char_span(start, end, label=label)

                if(span == None):
                    continue

                entities.append(span)



        doc.ents = entities
        #db.add(doc)

    #db.to_disk('./train.spacy')


if __name__ == '__main__':
    train()
