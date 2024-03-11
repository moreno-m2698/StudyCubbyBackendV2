from fastapi import APIRouter, HTTPException, Response
from src.services import Image_Service
import asyncio
import boto3

track_router = APIRouter()
image_service = Image_Service()


@track_router.get("/tracks/")
async def get_tracks():
    try:
        # Get image object from S3
        response = await image_service.get_image()

        # Check if response is successful
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise HTTPException(status_code=500, detail="Failed to retrieve image from S3")

        # Return image content
        image_data = response['Body'].read()

        # Return the image data with appropriate content type
        return {
            "Content-Type": response['ContentType'],
            "body": image_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
s3_client = boto3.client("s3")
@track_router.get("/images/")
async def get_image_from_s3():
    try:
        # Get image object from S3
        response = s3_client.get_object(
            Bucket="fed-alpaca",
            Key="test.jpg"
        )

        # Check if response is successful
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise HTTPException(status_code=500, detail="Failed to retrieve image from S3")

        # Return image content
        image_data = response['Body'].read()
        print(image_data)

        # Return the image data with appropriate content type
        return {
            "Content-Type": response['ContentType'],
            "body": image_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))