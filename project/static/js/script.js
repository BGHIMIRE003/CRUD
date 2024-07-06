document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('addAppointment').addEventListener('click', () => {
        const form = document.getElementById('appointmentForm');
        const newRow = document.createElement('div');
        newRow.classList.add('form-row');
        newRow.innerHTML = `
            <div class="col-md-3">
                <label for="firstName" class="form-label">First Name</label>
                <input type="text" name="firstName" class="form-control" required>
            </div>
            <div class="col-md-3">
                <label for="lastName" class="form-label">Last Name</label>
                <input type="text" name="lastName" class="form-control" required>
            </div>
            <div class="col-md-2">
                <label for="dob" class="form-label">DOB</label>
                <input type="text" name="dob" class="form-control" placeholder="MM/DD/YYYY" required>
            </div>
            <div class="col-md-2">
                <label for="reason" class="form-label">Reason</label>
                <input type="text" name="reason" class="form-control" required>
            </div>
            <div class="col-md-2">
                <label for="appointmentDate" class="form-label">Appointment Date</label>
                <input type="text" name="appointmentDate" class="form-control" placeholder="MM/DD/YYYY" required>
            </div>
            <div class="col-md-1">
                <label for="time" class="form-label">Time</label>
                <input type="text" name="time" class="form-control" placeholder="HH:MM" required>
            </div>
            <div class="col-md-1">
                <div class="btn-container">
                    <button type="submit" class="btn btn-submit">Submit</button>
                    <button type="button" class="btn btn-edit" onclick="editRecord()">Edit</button>
                    <button type="button" class="btn btn-danger" onclick="deleteRecord()">Delete</button>
                </div>
            </div>
        `;
        form.insertBefore(newRow, document.querySelector('.add-appointment-container'));
    });
});

function searchRecords() {
    const lastName = document.getElementById('searchName').value;
    alert(`Searching for records with Last Name: ${lastName}`);
}

function editRecord() {
    alert('Edit functionality not implemented yet.');
}

function deleteRecord() {
    alert('Delete functionality not implemented yet.');
}
