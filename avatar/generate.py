import os
from django.conf import settings
from PIL import Image
from .models import Avatar
import numpy as np
import hashlib
from . import probability as prob
import random
from io import BytesIO
from django.core.files import File
from django.contrib import messages


# Keep track of punk metadata
allmetadata = []
# Keep track of punks created
punksCreated = 0
# Keep track of filehashes
fileHashes = []

# Punks
# Male = punks[0:4], Female = punks[4:8], Alien = punks[8],
# Ape = punks[9], Zombie = punks[10]
punks = [
    'punk01.png', 'punk02.png', 'punk03.png', 'punk04.png',
    'punk05.png', 'punk06.png', 'punk07.png', 'punk08.png',
    'punk09.png', 'punk10.png', 'punk11.png'
    ]
punkTypes = ['male', 'female', 'alien', 'ape', 'zombie']
backgrounds = ['bg01.png', 'bg02.png', 'bg03.png']
smokes = ['smoke01.png', 'smoke02.png', 'smoke03.png']


def get_punk_and_attributes(punk_type):
    """
    Get a random punk image and its associated
    attributes for the specified punk_type.
    """
    attrDict_mapping = {
        'male': prob.maleAttr,
        'female': prob.femaleAttr,
        'alien': prob.alienAttr,
        'ape': prob.apeAttr,
        'zombie': prob.zombieAttr
    }
    punk_path_mapping = {
        'male': os.path.join(
            settings.MEDIA_ROOT, f"punks/{random.choice(punks[0:4])}"),
        'female': os.path.join(
            settings.MEDIA_ROOT, f"punks/{random.choice(punks[4:8])}"),
        'alien': os.path.join(
            settings.MEDIA_ROOT, f"punks/{punks[8]}"),
        'ape': os.path.join(
            settings.MEDIA_ROOT, f"punks/{punks[9]}"),
        'zombie': os.path.join(
            settings.MEDIA_ROOT, f"punks/{punks[10]}")
    }
    return Image.open(
        punk_path_mapping[punk_type]), attrDict_mapping[punk_type]


def generate_and_save_punk_for_user(user, request):
    """
    Generate and save a new punk image with
    random attributes for the given user.
    """
    punkTypes = ['male', 'female', 'alien', 'ape', 'zombie']
    backgrounds = os.listdir(
        os.path.join(settings.MEDIA_ROOT, 'backgrounds'))
    smokes = os.listdir(
        os.path.join(settings.MEDIA_ROOT, 'attributes/uni/smoke'))

    punkType = np.random.choice(punkTypes, p=[0.5, 0.3, 0.05, 0.06, 0.09])
    punkStack, attrDict = get_punk_and_attributes(punkType)

    metadata = {'Punk Type': punkType.capitalize()}
    attributeCount = 0
    basedir = f"attributes/{punkType}/"

    # Metadata dictionary to keep track of attributes
    metadata = {}

    if punkType == 'male':
        attrDict = prob.maleAttr
        punkStack = Image.open(
            os.path.join(
                settings.MEDIA_ROOT, f"punks/{random.choice(punks[0:4])}"))
        metadata['Punk Type'] = 'Male'
    elif punkType == 'female':
        attrDict = prob.femaleAttr
        punkStack = Image.open(
            os.path.join(
                settings.MEDIA_ROOT, f"punks/{random.choice(punks[4:8])}"))
        metadata['Punk Type'] = 'Female'
    elif punkType == 'alien':
        attrDict = prob.alienAttr
        punkStack = Image.open(
            os.path.join(settings.MEDIA_ROOT, f"punks/{punks[8]}"))
        metadata['Punk Type'] = 'Alien'
    elif punkType == 'ape':
        attrDict = prob.apeAttr
        punkStack = Image.open(
            os.path.join(settings.MEDIA_ROOT, f"punks/{punks[9]}"))
        metadata['Punk Type'] = 'Ape'
    elif punkType == 'zombie':
        attrDict = prob.zombieAttr
        punkStack = Image.open(
            os.path.join(settings.MEDIA_ROOT, f"punks/{punks[10]}"))
        metadata['Punk Type'] = 'Zombie'

    basedir = f"attributes/{punkType}/"
    hasHeadAttr = np.random.choice([True, False], p=[0.7, 0.3])
    if hasHeadAttr:
        headAttrs = [
            f"{basedir}head/{item[0]}" for item in attrDict['head'].items()]
        headChoice = Image.open(
            os.path.join(
                settings.MEDIA_ROOT,
                np.random.choice(
                    headAttrs, p=list(attrDict['head'].values()))))
        punkStack.paste(headChoice, (0, 0), headChoice)
        attributeCount += 1
        metadata['Head Attribute'] = str(headChoice.filename.split("/")[-1])

    if punkType == 'male' or punkType == 'zombie':
        hasFacialHair = np.random.choice([True, False], p=[0.3, 0.7])
        if hasFacialHair:
            facialHairAttrs = [
                f"{basedir}facialhair/{item[0]}" for item in attrDict['facialhair'].items()]
            facialHairChoice = Image.open(
                os.path.join(
                    settings.MEDIA_ROOT,
                    np.random.choice(
                        facialHairAttrs,
                        p=list(attrDict['facialhair'].values()))))
            punkStack.paste(facialHairChoice, (0, 0), facialHairChoice)
            attributeCount += 1
            metadata['Facial Hair'] = str(
                facialHairChoice.filename.split("/")[-1])

    hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
    if hasGlasses:
        glassesAttrs = [
            f"{basedir}eyes/{item[0]}" for item in attrDict['eyes'].items()]
        if glassesAttrs:
            glassesChoice = Image.open(
                os.path.join(
                    settings.MEDIA_ROOT,
                    np.random.choice(
                        glassesAttrs, p=list(attrDict['eyes'].values()))))
            punkStack.paste(glassesChoice, (0, 0), glassesChoice)
            attributeCount += 1
            metadata['Glasses'] = str(glassesChoice.filename.split("/")[-1])

    hasMouthModifier = np.random.choice([True, False], p=[0.6, 0.4])
    if hasMouthModifier:
        mouthAttrs = [
            f"{basedir}mouth/{item[0]}" for item in attrDict['mouth'].items()]
        if mouthAttrs:
            mouthChoice = Image.open(
                os.path.join(
                    settings.MEDIA_ROOT,
                    np.random.choice(
                        mouthAttrs, p=list(attrDict['mouth'].values()))))
            punkStack.paste(mouthChoice, (0, 0), mouthChoice)
            attributeCount += 1
            metadata['Mouth Modifier'] = str(
                mouthChoice.filename.split("/")[-1])

    hasMask = np.random.choice([True, False], p=[0.025, 0.975])
    if not hasMask:
        hasSmoke = np.random.choice([True, False], p=[0.25, 0.75])
        if hasSmoke:
            smokeChoice = Image.open(
                os.path.join(
                    settings.MEDIA_ROOT,
                    f"attributes/uni/smoke/{np.random.choice(smokes, p=[0.33, 0.33, 0.34])}"))
            punkStack.paste(smokeChoice, (0, 0), smokeChoice)
            attributeCount += 1
            metadata['Smoking'] = str(smokeChoice.filename.split("/")[-1])

    if hasMask and punkType != 'ape':
        maskChoice = Image.open(
            os.path.join(settings.MEDIA_ROOT, f"{basedir}mask/mask01.png"))
        punkStack.paste(maskChoice, (0, 0), maskChoice)
        attributeCount += 1
        metadata['Wearing Mask'] = str(maskChoice.filename.split("/")[-1])

    hasEarring = np.random.choice([True, False], p=[0.15, 0.85])
    if hasEarring:
        earringChoice = Image.open(
            os.path.join(
                settings.MEDIA_ROOT, f"{basedir}earring/earring01.png"))
        punkStack.paste(earringChoice, (0, 0), earringChoice)
        attributeCount += 1
        metadata['Earrings'] = str(earringChoice.filename.split("/")[-1])

    hasNecklace = np.random.choice([True, False], p=[0.2, 0.8])
    if hasNecklace:
        neckAttrs = [
            f"{basedir}neck/{item[0]}" for item in attrDict['neck'].items()]
        if neckAttrs:
            neckChoice = Image.open(
                os.path.join(
                    settings.MEDIA_ROOT,
                    np.random.choice(
                        neckAttrs, p=list(attrDict['neck'].values()))))
            punkStack.paste(neckChoice, (0, 0), neckChoice)
            attributeCount += 1
            metadata['Neck Modifier'] = str(neckChoice.filename.split("/")[-1])

    metadata['Total Attributes'] = attributeCount
    allmetadata.append(metadata)

    fileHash = hashlib.md5(punkStack.tobytes())
    hashDigest = fileHash.hexdigest()
    punkBg = Image.open(
        os.path.join(
            settings.MEDIA_ROOT,
            f"backgrounds/{np.random.choice(backgrounds, p=[0.7, 0.2, 0.1])}"))
    punkBg.paste(punkStack, (0, 0), punkStack)
    punkFilename = f"{hashDigest}.png"
    buff = BytesIO()
    punkBg.save(buff, format='PNG')

    avatar = Avatar(user=user, punk_type=punkType, attributes=metadata)
    avatar.image.save(punkFilename, File(buff), save=True)
    if request:
        messages.success(
            request, 'Horray, your new  aiPunk was generated successfully!')

    return punkStack
