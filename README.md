# Vulnerability Intelligence Tracker

CVE'de boşluk vs olunca da unique olmuyor. CVE'lerin unique olması için bir şeyler yapılabilir mi?
CVSS kontrolü yapılabilir mi?

## To-Do
- [ ] Sending Errors by Email: [Part VII Error Handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)
- [ ] Login: [Part V User Logins](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- [ ] User Profile: [Part VI Profile Page](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
- [ ] Moment Last Login etc.: [Part XII Dates and Times](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-dates-and-times)
- [ ] Password Reset: [Part X Email Support](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
- [ ] Database Relationships: [Part IV Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) & [Part VIII Followers](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers)
- [ ] Pagination: [Part IX Pagination](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
- [ ] Multithread: [Part XXII Background Jobs](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)
- [ ] Search: [Part XVI Full-Text Search](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)
- [ ] Pop-up / Pop-over: [Part XX Some Javascript Magic](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xx-some-javascript-magic)
- [ ] Deployment: [Part XVII Deployment on Linux](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux) & [Part XVIII Deployment on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku) & [Part XIX Deployment on Docker Containers](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)
- [ ] API: [Part XXIII API](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis)

## Dev Notes

### Setup Virtual Environment

```bash
python3 -m venv .venv
```

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run App

```bash
flask run --debug
```

---

### Database Initialization

DB initialization is only required once(first time).

```bash
flask db init
```

### Database Migration

DB migration is required when there is a change in the DB schema.
Migrate command does not apply the changes to the DB, it only generates the migration script.

```bash
flask db migrate -m "migration message"
```

### Database Upgrade

DB upgrade is required to apply the migration script to the DB.

```bash
flask db upgrade
```
