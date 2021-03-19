$(document).ready(function () {
    let form = $('#js-main-form');
    let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
    let stepperWizard = new Stepper($('#stepper4')[0], { animation: true });

    let session_id = null;

    let get_values = function (object_list) {
        let obj = {};
        let arr = [];

        object_list.forEach(function (data) {
            if (obj.hasOwnProperty(data.name)) {
                if (Array.isArray(obj[data.name]))
                    obj[data.name].push(data.value);
                else {
                    arr = [obj[data.name]];
                    arr.push(data.value);

                    obj[data.name] = arr;
                }
            } else {
                obj[data.name] = data.value;
            }
        });
        return obj;
    };

    let stepperMoveToNext = function (position) {
        if (position === null)
            stepperWizard.next();
        else
            stepperWizard.to(parseInt(position));
    };

    function drawWorkExperience(data) {
        const item = `
            <div>
                <div class="row">
                    <div class="col-3"><img src="" alt="img here"></div>
                    <div class="col">
                        <h4>${data.company_name}</h4>
                        <div>${data.title}</div>
                        <div>${data.date_started} - ${data.date_ended}</div>
                    </div>
                </div>
            </div>
            <hr/>
        `;
        $(item).appendTo('#js-user-work-experiences');
        return $(item);
    }

    $('.js-save-work-experience-btn').click(function (event) {
        let data = form.find('.js-work-experience').serializeArray();
        data = get_values(data);

        $.ajax({
            "url": save_work_experience_url,
            "headers": {"X-CSRFToken": csrf_token},
            "type": "post",
            "data": {
                "session_id": session_id,
                "data": JSON.stringify(data)
            },
            "success": (resp) => {
                if (resp.status === "error") {
                    alert(resp.message);
                } else {
                    drawWorkExperience(resp.experience)
                }
            }
        });
    });

    $('.js-stepper-next-btn').click(function (event) {
        let $btn = $(event.target);
        let position = $btn.data("stepper-position");
        let stepInputFieldsClass = $btn.data('current-step');
        let inputValidity = true;

        document.querySelectorAll(`.${stepInputFieldsClass}`).forEach(function (field) {
            if (field.checkValidity)
                inputValidity = inputValidity && field.checkValidity();
        });

        if (stepInputFieldsClass.length > 0 && !inputValidity) {
            $('#dummy-submit-btn').click();
            return;
        }

        let data = null;

        switch (stepInputFieldsClass) {
            case "js-job-title":
                data = form.find(`.${stepInputFieldsClass}`).serializeArray();
                data = get_values(data);

                $.ajax({
                    "url": save_job_title_url,
                    "headers": {"X-CSRFToken": csrf_token},
                    "type": "post",
                    "data": data,
                    "success": (resp) => {
                        if (resp.status === "error") {
                            alert(resp.message);
                        } else {
                            session_id = resp.session_id;
                            stepperMoveToNext(position);
                        }
                    }
                });
                break;
            case "js-work-experience":
                stepperMoveToNext(position);
                break;
            case "js-opportunity":
                data = form.find(`.${stepInputFieldsClass}`).serializeArray();
                data = get_values(data);
                 $.ajax({
                    "url": save_opportunity_url,
                    "headers": {"X-CSRFToken": csrf_token},
                    "type": "post",
                    "data": {"data": JSON.stringify(data), "session_id": session_id},
                    "success": (resp) => {
                        if (resp.status === "error") {
                            alert(resp.message);
                        } else {
                            stepperMoveToNext(position);
                        }
                    }
                });
                break;
        }
    });
});