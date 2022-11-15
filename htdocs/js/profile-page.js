const USER_PROFILE = {
    firstName: "I",
    lastName: "Popescu",
    lastActiveAt: "2022-10-31 23:54:32",
    rating: 3.4,
    location: "Bucharest",
    email: "ip@email.com",
    isEmailVisible: false,
    handsPlayed: 345,
    winRate: 0.35,
    bio: "This is my bio."
}

function getLastActiveAt(dateString) {
    // procesez stringul pt a obtine o anumita valoare 
    return dateString;
}

function createRatingString(rating) {
    if (rating > 0) {
        const ratingString = `${rating}/5`;
        return ratingString;
    }
    return "0/5";
}
function createLocationString(location) {
    if (location) {
        const locationString = `Locatie: ${location}`
        return locationString;
    } 
    return `Locatie: Necunoscuta`;
}

function createEmailString(email, isVisible=true) {
    if (isVisible) {
        const emailString = `Email: ${email}`;
        return emailString;
    }
    return "Email: Ascuns";
}

function createWinRateString(winRate) {
    const winRatePerc = winRate * 100;
    const winRateString = `${winRatePerc}%`;
    return winRateString; 
}

const playerName = document.getElementById("player-name-span");
playerName.innerText = `${USER_PROFILE.firstName} ${USER_PROFILE.lastName}`;

const playerLastActiveAt = document.getElementById("player-last-active-at-span");

const lastActiveAt = getLastActiveAt(USER_PROFILE.lastActiveAt);
playerLastActiveAt.innerText = lastActiveAt;

// playerLastActiveAt.innerText = getLastActiveAt(USER_PROFILE.lastActiveAt);

const playerRating = document.getElementById("player-rating-span");
playerRating.innerText = createRatingString(USER_PROFILE.rating);

const playerLocation = document.getElementById("player-location-span");
playerLocation.innerText = createLocationString(USER_PROFILE.location);

const playerEmail = document.getElementById("player-email-span");
playerEmail.innerText = createEmailString(USER_PROFILE.email, USER_PROFILE.isEmailVisible);

const playerHandsSpan = document.getElementById("player-hands-span");
playerHandsSpan.innerText = USER_PROFILE.handsPlayed;

const playerWinRate = document.getElementById("player-win-rate-span");
playerWinRate.innerText = createWinRateString(USER_PROFILE.winRate);

const playerBio = document.getElementById("player-bio-paragraph");
playerBio.innerText = USER_PROFILE.bio;