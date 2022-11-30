
{
    const inputTags = ['BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'];
    const modelName = document.getElementById('django-admin-form-add-constants').dataset.modelName;
    if (modelName) {
        const form = document.getElementById(modelName + '_form');
        for (const element of form.elements) {
            // HTMLElement.offsetParent returns null when the element is not
            // rendered.
            if (inputTags.includes(element.tagName) && !element.disabled && element.offsetParent) {
                element.focus();
                break;
            }
        }
    }
    var input0 = document.getElementById('id_organization_other');
    var input1 = document.getElementById('id_organization');
    var input2 = document.getElementById('id_phone');
    var input3 = document.getElementById('id_email');

    fetch('/static/data.json')
    .then(res => res.json())
    .then(data => {
        input1.addEventListener('input', function (e) {
        var value = String(e.target.value);
        if(value) {
            input2.value = data.organization.find( record => record.name === value).tel;
            input3.value = data.organization.find( record => record.name === value).email;
            input0.style.display = 'none';
        } else {
            input2.value = '';
            input3.value = '';
            input0.style.display = 'block';
        }
        });
    })
}

