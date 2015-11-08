import Decimal from 'decimal.js';

export const width = 107;
export const height = 17;

// Decimal constructors for base 2 and base 10 numbers
const BigBinary = Decimal.constructor({ precision: width * height });
const BigDecimal = Decimal.constructor({ precision: 550 });

function big(n) {
  return new BigDecimal(n);
}

function bigBinary(n) {
  return new BigBinary(n)
}

function* range2d(n, m) {
  for(let i=0; i < n; i += 1) {
    for(let j=0; j < m; j += 1) {
      yield[i, j];
    }
  }
}

// Left pad a string to at least length `length`
function zeroFill(string, length, pad="0") {
  const padLength = length - string.length;
  return padLength > 0 
    ? `${pad.repeat(padLength)}${string}`
    : string;
}

export const k = "960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719";

// Generator for direct bitmap decode
// n: numeric string
export function* decode(n) {
  const binaryInput = bigBinary(n).div(17).toString(2);
  const bits = zeroFill(binaryInput, width * height);

  for(let [x, y] of range2d(width, height)) {
    const index = x * height + y;

    // invert y axis
    yield [x, height - y - 1, +bits[index]];
  }
}

// Generator for iterative Tupper formula
// n: numeric string
export function* tupperFormula(n) {
  const two = big(2);
  const N = big(n);

  for(let [x, y] of range2d(width, height)) {
    const value = N.plus(y).div(17).times(two.pow(-17 * x - y)).mod(2).gt(1);

    // invert x axis
    yield [width - x - 1, y, value];
  } 
}

// Test driver
// [0,0] bottom-left
const buffer = Array(height);
for(let i = 0; i < height; i ++) {
  buffer[i] = Array(width);
}

//const result = decode(k);
const result = tupperFormula(k);

for(let [x, y, z] of result) {
  buffer[y][x] = z ? "##" : "  "; 
}

const output = buffer.map(row => row.join("")).join("\n");
console.log(output);
