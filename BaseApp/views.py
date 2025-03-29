# BaseApp/views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .db_session import create_session
from .models import Star
import sqlalchemy as sa
from datetime import date

async def star_list(request: HttpRequest):
    async with await create_session() as session:
        stars = await session.execute(sa.select(Star).where(Star.publish == True))
        return render(request, 'star_list.html', {
            'stars': stars.scalars().all()
        })

async def add_star(request: HttpRequest):
    if request.method == 'POST':
        form_data = request.POST
        async with await create_session() as session:
            new_star = Star(
                name=form_data['name'],
                bio=form_data.get('bio', ''),
                birth_date=date.fromisoformat(form_data['birth_date']),
                profession=form_data['profession'],
                country=form_data.get('country', ''),
                photo_url=form_data.get('photo_url', '')
            )
            session.add(new_star)
            await session.commit()
            return redirect('star_list')
    return render(request, 'add_star.html')