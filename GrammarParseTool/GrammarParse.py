#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re


class Slot:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        pass


class Intent:
    def __init__(self, name, samples):
        self.name = name
        self.samples = samples
        self.containSlot = False
        self.intent_slots = []
        pass

    def appendSlots(self, data):
        self.intent_slots.append(data)
        self.containSlot = True


class SlotBean:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        pass


slots = []
intents = []


def init():
    f = open('menu.json', 'r')
    grammar = json.load(f)
    slot_types = grammar['slot_types']
    all_intents = grammar['intents']

    for slot in slot_types:
        s = Slot(slot['name'], slot['values'])
        slots.append(s)

    for intent in all_intents:
        i = Intent(intent['name'], intent['samples'])
        try:
            for lsb in intent['slots']:
                print lsb['name'], lsb['type']
                bean = SlotBean(lsb['name'], lsb['type'])
                i.appendSlots(bean)
            print lsb['name'], i.containSlot
        except:
            pass
        intents.append(i)


def query(param):
    for intent in intents:
        if not intent.containSlot:
            if param in intent.samples:
                print intent.name
                break
        else:
            print 'contain slot', intent.name
            print intent.samples[0]
            matchObj = re.match(r'{',intent.samples[0])
            # matchObj = re.match(u'{[\s\S]*}',intent.samples[0])
            if matchObj:
                print matchObj.group()
            else:
                print "No Match"
            pass


init()
query(u'不点');
