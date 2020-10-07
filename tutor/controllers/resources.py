from .. import db
from flask import render_template, redirect, url_for
from ..models.course import Resource
from .forms.resource_form import ResourceForm


def newResource(id):
    form = ResourceForm()
    if form.validate_on_submit():
        resource = Resource(title=form.title.data,
                            content=form.content.data, link=form.link.data, course_id=id)
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for('get_course_info_route', id=id))
    return render_template('resource.html', form=form)
