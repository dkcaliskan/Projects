// input your note and total note of exam

const calculate = function (note, totalNote) {
    const percent = (note / totalNote) * 100
    let grade = ''

    if (percent >= 90) {
        grade = 'A'
    }
    else if (percent >= 80) {
        grade = 'B'
    }
    else if (percent >= 70) {
        grade = 'C'
    }
    else if (percent >= 60) {
        grade = 'D'
    }
    else {
        grade = 'F'
    }
    return `You got a ${grade} (${percent}%)!`
}
console.log(calculate(15, 20))
