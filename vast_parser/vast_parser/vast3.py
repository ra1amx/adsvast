import dexml
from dexml import fields

"""
MediaFile Model
VAST 3.0
"""
class MediaFile(dexml.Model):
    id = fields.String(required=False)
    delivery = fields.String()
    type = fields.String()

    bitrate = fields.String(required=False)
    minBitrate = fields.String(required=False)
    maxBitrate = fields.String(required=False)

    width = fields.String()
    height = fields.String()
    scalable = fields.Boolean(required=False)
    maintainAspectRatio = fields.Boolean(required=False)

    codec = fields.String(required=False)
    apiFramework = fields.String(required=False)

    mediaFileUrl = fields.CDATA(tagname=".")

"""
Linear Model
VAST 3.0
"""
class Linear(dexml.Model):
    skipoffset = fields.String()

    duration = fields.String(tagname="Duration")
    mediaFiles = fields.List(MediaFile, tagname="MediaFiles")

"""
Creative Model
VAST 3.0
"""
class Creative(dexml.Model):
    id = fields.String(required=False)
    sequence = fields.String(required=False)
    apiFramework = fields.String(required=False)

    linear = fields.Model(Linear, required=False)

"""
Tracking Model
VAST 3.0
"""
class Tracking(dexml.Model):
    event = fields.String(attrname="event")

    trackingUrl = fields.CDATA(tagname=".")

"""
VideoClicks Model
VAST 3.0
"""
class VideoClicks(dexml.Model):
    clickThrough = fields.CDATA(tagname="ClickThrough", required=False)
    clickTracking = fields.CDATA(tagname="ClickTracking", required=False)
    customClick = fields.CDATA(tagname="CustomClick", required=False)

"""
InLine Model
VAST 3.0
"""
class InLine(dexml.Model):
    adSystem = fields.String(tagname="AdSystem")
    adTitle = fields.String(tagname="AdTitle")
    adServingId = fields.String(tagname="AdServingId")

    impression = fields.CDATA(tagname="Impression")

    trackingEvents = fields.List(Tracking, tagname="TrackingEvents", required=False)
    videoClicks = fields.Model(VideoClicks, tagname="VideoClicks", required=False)
    creatives = fields.List(Creative, tagname="Creatives")


"""
Wrapper Model
VAST 3.0
"""
class Wrapper(dexml.Model):
    adSystem = fields.String(tagname="AdSystem")
    impression = fields.CDATA(tagname="Impression")
    vastAdTagURI = fields.CDATA(tagname="VASTAdTagURI")

"""
Ad Model
VAST 3.0
"""
class Ad(dexml.Model):
    id = fields.String(required=False)
    sequence = fields.String(required=False)

    inLine = fields.Model(InLine, required=False)
    wrapper = fields.Model(Wrapper, required=False)

"""
VAST Model
VAST 3.0
"""
class VAST(dexml.Model):
    version = fields.String()
    errorData = fields.CDATA(tagname="Error", required=False)

    ad = fields.Model(Ad, required=False)